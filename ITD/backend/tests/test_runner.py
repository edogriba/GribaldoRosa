import requests
from colorama import Fore, Style, init
import re
import yaml

def parse_test_file(file_path):
    """
    Parses a test file and extracts test cases.
    The test file should contain test cases separated by '###'. Each test case should have the following format:
    - A description line
    - A method and URL line (e.g., "GET /api/resource")
    - Optional headers (e.g., "Content-Type: application/json")
    - Optional body in JSON format
    - Expected response prefixed with "Response:" and followed by the expected JSON response
    
    Args:
        file_path (str): The path to the test file.
    
    Returns:
        list: A list of dictionaries, each representing a test case with the following keys:
            - 'description' (str): The description of the test case.
            - 'method' (str): The HTTP method (e.g., GET, POST).
            - 'url' (str): The URL for the request.
            - 'headers' (dict): The headers for the request.
            - 'body' (dict or list, optional): The JSON body for the request.
            - 'expected_response' (dict or list): The expected JSON response.
    
    Example test file content:
    ### Test GET request
    GET /api/resource
    Content-Type: application/json
    Response: {"status": "success"}
    
    ### Test POST request
    POST /api/resource
    Content-Type: application/json
    {"name": "Alice"}
    Response: {"status": "success", "data": {"name": "Alice"}}
    
    Example output:
    [
        {
            'description': 'Test GET request',
            'method': 'GET',
            'url': '/api/resource',
            'headers': {'Content-Type': 'application/json'},
            'body': None,
            'expected_response': {'status': 'success'}
        },
        {
            'description': 'Test POST request',
            'method': 'POST',
            'url': '/api/resource',
            'headers': {'Content-Type': 'application/json'},
            'body': {'name': 'Alice'},
            'expected_response': {'status': 'success', 'data': {'name': 'Alice'}}
        }
    ]
    """
    with open(file_path, 'r') as file:
        content = file.read()
    test_cases_raw = re.split(r'###\s*', content)
    test_cases = []
    for test_raw in test_cases_raw:
        test_raw = test_raw.strip()

        if not test_raw:
            continue
        lines = [line.strip() for line in test_raw.splitlines() if line.strip()]

        if not lines:
            continue
        description = lines[0]
        method_url = lines[1]
        method_url_parts = method_url.split()

        if len(method_url_parts) != 2:
            continue
        method, url = method_url_parts
        headers = {}
        body = None
        expected_response = None
        i = 2
        while i < len(lines):
            line = lines[i]
            if line.startswith('Content-Type:'):
                header_name, header_value = line.split(':', 1)
                headers[header_name.strip()] = header_value.strip()
                i += 1
            elif line.startswith('{') or line.startswith('['):
                body_lines = []
                while i < len(lines) and not lines[i].startswith('Response:'):
                    body_lines.append(lines[i])
                    i += 1
                body_raw = '\n'.join(body_lines)
                body = parse_json_with_types(body_raw)
            elif 'Response:' in line:
                response_content = line.partition('Response:')[2].strip()
                if response_content:
                    expected_response_lines = [response_content]
                    i += 1
                    while i < len(lines):
                        expected_response_lines.append(lines[i])
                        i += 1
                else:
                    i += 1
                    expected_response_lines = lines[i:]
                    i = len(lines)
                expected_response_raw = '\n'.join(expected_response_lines)
                expected_response = parse_json_with_types(expected_response_raw)
                break
            else:
                i += 1
        test_cases.append({
            'description': description,
            'method': method,
            'url': url,
            'headers': headers,
            'body': body,
            'expected_response': expected_response
        })
    return test_cases


def parse_json_with_types(raw_input):
    """
    Parses a JSON string with type annotations and converts it to a Python object.
    The type annotations are used to convert the values to the correct types.
    Args:
        raw_input (str): The JSON string with type annotations.
    Returns:
        dict or list: The parsed JSON object.

    Example:
    Input:
    {
        "name": string,
        "age": integer,
        "height": float,
        "is_student": boolean,
        "address": null
    }

    Output:
    {
        "name": "string",
        "age": 0,
        "height": 0.0,
        "is_student": False,
        "address": None
    }
    """
    raw_input = re.sub(r",\s*([\]}])", r"\1", raw_input)
    raw_input = re.sub(r'(?<=:\s)(string|integer|float|boolean|null)(?=[,\s}])', r'"\1"', raw_input)
    try:
        data = yaml.safe_load(raw_input)
        data = mark_placeholders(data)
        return data
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return raw_input.strip()


def mark_placeholders(data):
    """
    Recursively marks placeholders in the data with their respective types.
    Args:
        data (dict, list, str, int, float, bool, None): The data to process.
    Returns:
        dict, list, str, int, float, bool, None: The data with placeholders marked.

    Example:
    Input:
    {
        "name": "string",
        "age": 0,
        "is_student": boolean,
        "address": null
    }

    Output:
    {
        "name": "__TYPE_string__",
        "age": "__TYPE_integer__",
        "is_student": "__TYPE_boolean__",
        "address": "__TYPE_null__"
    }
    """
    if isinstance(data, dict):
        return {k: mark_placeholders(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [mark_placeholders(v) for v in data]
    elif isinstance(data, str):
        if data.strip() in ['string', 'integer', 'float', 'boolean', 'null']:
            return f'__TYPE_{data.strip()}__'
        return data
    else:
        return data


def compare_responses(actual, expected, path=''):
    """
    Compares the actual and expected responses recursively.
    Args:
        actual (dict, list, str, int, float, bool, None): The actual response data.
        expected (dict, list, str, int, float, bool, None): The expected response data.
        path (str): The path to the current data in the response.
    Returns:
        bool: True if the actual response matches the expected response, False otherwise.
    """
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            print(f"{Fore.RED}Type mismatch at {path}: expected dict, got {type(actual).__name__}{Style.RESET_ALL}")
            return False
        for key in expected:
            if key not in actual:
                print(f"{Fore.RED}Missing key at {path}: '{key}' not found in actual response{Style.RESET_ALL}")
                return False
            if not compare_responses(actual[key], expected[key], path=path+'.'+key):
                return False
        return True
    elif isinstance(expected, list):
        if not isinstance(actual, list):
            print(f"{Fore.RED}Type mismatch at {path}: expected list, got {type(actual).__name__}{Style.RESET_ALL}")
            return False
        if len(actual) != len(expected):
            print(f"{Fore.RED}Length mismatch at {path}: expected {len(expected)}, got {len(actual)}{Style.RESET_ALL}")
            return False
        for idx, (a_item, e_item) in enumerate(zip(actual, expected)):
            if not compare_responses(a_item, e_item, path=f"{path}[{idx}]"):
                return False
        return True
    elif isinstance(expected, str):
        if expected.startswith('__TYPE_') and expected.endswith('__'):
            expected_type = expected[7:-2]
            type_checks = {
                'string': lambda x: isinstance(x, str),
                'integer': lambda x: isinstance(x, int),
                'float': lambda x: isinstance(x, float),
                'boolean': lambda x: isinstance(x, bool),
                'null': lambda x: x is None,
            }
            result = type_checks.get(expected_type, lambda x: False)(actual)
            if not result:
                print(f"{Fore.RED}Type mismatch at {path}: expected {expected_type}, got {type(actual).__name__}{Style.RESET_ALL}")
            return result
        else:
            if actual != expected:
                print(f"{Fore.RED}Value mismatch at {path}: expected '{expected}', got '{actual}'{Style.RESET_ALL}")
                return False
            return True
    elif isinstance(expected, (int, float)):
        if not isinstance(actual, (int, float)):
            print(f"{Fore.RED}Type mismatch at {path}: expected numeric, got {type(actual).__name__}{Style.RESET_ALL}")
            return False
        if expected == 0:
            result = actual == 0
        else:
            tolerance = 0.20 * abs(expected)
            difference = abs(actual - expected)
            result = difference <= tolerance
            if not result:
                print(f"{Fore.RED}Value mismatch at {path}: expected {expected} ± {tolerance}, got {actual} (difference {difference}){Style.RESET_ALL}")
        return result
    else:
        result = actual == expected
        if not result:
            print(f"{Fore.RED}Value mismatch at {path}: expected '{expected}', got '{actual}'{Style.RESET_ALL}")
        return result


def normalize_whitespace(s):
    """
    Normalizes whitespace in a string by removing leading/trailing spaces and collapsing multiple spaces into a single space.
    Args:
        s (str): The input string.
    Returns:
        str: The string with normalized whitespace.

    Example:
    Input: "  hello   world  "
    Output: "hello world"
    
    Input: "hello\n\nworld"
    Output: "hello world"
    """
    return ' '.join(s.strip().split())


def run_tests(test_cases):
    """
    Runs the test cases and prints the results.
    Args:
        test_cases (list): A list of test cases.
    Raises:
        Exception: If any test case fails.
    """
    total_tests = len(test_cases)
    passed_tests = 0
    for i, test in enumerate(test_cases, start=1):
        description = test['description']
        method = test['method']
        url = test['url']
        headers = test['headers']
        body = test['body']
        expected_response = test['expected_response']
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"Test {i}/{total_tests}: {description}")
        print(f"URL: {url}")
        try:
            if method.upper() == 'POST':
                response = requests.post(url, json=body, headers=headers)
            elif method.upper() == 'GET':
                response = requests.get(url, headers=headers)
            else:
                print(f"{Fore.YELLOW}{description}: UNSUPPORTED METHOD {method}{Style.RESET_ALL}")
                continue
            if 'application/json' in response.headers.get('Content-Type', ''):
                actual_response = response.json()
            else:
                actual_response = response.text.strip()
            if isinstance(expected_response, dict):
                print("Comparing responses...")
                if compare_responses(actual_response, expected_response):
                    print(f"{Fore.GREEN}{description}: PASS{Style.RESET_ALL}")
                    passed_tests += 1
                else:
                    print(f"{Fore.RED}{description}: FAIL{Style.RESET_ALL}")
                    print(f"Expected: {expected_response}\nGot: {actual_response}")
                    print(f"Request headers sent: {headers}")
                    print(f"Request body sent: {body}")
            else:
                expected_normalized = normalize_whitespace(expected_response)
                actual_normalized = normalize_whitespace(actual_response)
                if expected_normalized == actual_normalized:
                    print(f"{Fore.GREEN}{description}: PASS{Style.RESET_ALL}")
                    passed_tests += 1
                else:
                    print(f"{Fore.RED}{description}: FAIL{Style.RESET_ALL}")
                    print(f"Expected: {expected_response}\nGot: {actual_response}")
                    print(f"Request headers sent: {headers}")
                    print(f"Request body sent: {body}")
        except Exception as e:
            print(f"{Fore.RED}{description}: ERROR{Style.RESET_ALL}")
            print(f"Error: {e}")
            print(f"Request headers sent: {headers}")
            print(f"Request body sent: {body}")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print(f"Summary: {Fore.GREEN}{passed_tests}{Style.RESET_ALL}/{Fore.YELLOW}{total_tests}{Style.RESET_ALL} tests passed.")
    if passed_tests != total_tests:
        raise Exception(f"{total_tests - passed_tests} tests failed.")


if __name__ == '__main__':
    init()
    test_file = 'requests_&_responses.http'
    test_cases = parse_test_file(test_file)
    run_tests(test_cases)