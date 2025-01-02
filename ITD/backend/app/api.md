# S&C Analysis API Specification

## Table of Contents

- [S&C Analysis API Specification](#s&c-analysis-api-specification)
  - [Table of Contents](#table-of-contents)
  - [Endpoints](#endpoints)
    - [1. Get universities List](#1-get-universities-list)
      - [Response](#response)
    - [2. Get students List](#2-get-students-list)
      - [Response](#response)
    - [3. University Registration](#3-university-registration)
      - [Request Parameters](#request-parameters)
      - [Response](#response)
    - [4. Student Registration](#4-student-registration)
      - [Request Parameters](#request-parameters)
      - [Response](#response)

## Endpoints

### 1. Get universities List

- **Endpoint**: `universitylist`
- **Method**: `GET`
- **Description**: Retrieves a list of universities with their IDs and names.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `id` (integer): ID of the university.
    - `name` (string): Name of the university.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (string): Type of error (`database_error`).
    - `message` (string): Error message.

<details>
<summary>Example Response</summary>

```json
[
  {
    "id": 1,
    "name": "MIT"
  },
  {
    "id": 2,
    "name": "Stanford University"
  }
]
```

</details>

------------------------------------------------

### 2. Get students List

- **Endpoint**: `studentlist`
- **Method**: `GET`
- **Description**: Retrieves a list of students with their IDs, names, and GPAs.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `id` (integer): ID of the student.
    - `firstName` (string): First name of the student.
    - `GPA` (float): GPA of the student.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (string): Type of error (`database_error`).
    - `message` (string): Error message.

<details>
<summary>Example Response</summary>

```json
[
  {
    "id": 1,
    "firstName": "Alice",
    "GPA": 3.9
  },
  {
    "id": 2,
    "firstName": "Bob",
    "GPA": 3.7
  }
]
```

</details>

------------------------------------------------

### 3. University Registration

- **Endpoint**: `/register/university`
- **Method**: `POST`
- **Description**: Registers a new university with required details.

#### Request Parameters

- **Body (JSON)**:
  - `university_mail` (string, required): Email of the university.
  - `university_password` (string, required): Password of the university.
  - `name` (string, required): Name of the university.
  - `location` (string, required): Location of the university.
  - `description` (string, required): Description of the university.
  - `logoPath` (string, optional): Path of the university's logo.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (string): Success message.
    - `token` (string): JWT token for authentication.
    - `user` (object): Registered user details.
      - `id` (integer): User ID.
      - `mail` (integer): User mail.
      - `name` (integer): User name.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (string): Type of the error(`invalid_request` or `conflict`).
    - `message` (string): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (string): Type of error (`server_error`).
    - `message` (string): Error message.
    
<details>
<summary>Example Request</summary>

```json
POST /register/university
{
  "university_email": "admin@mit.edu",
  "university_password": "securepassword",
  "name": "MIT",
  "location": "Cambridge, MA",
  "description": "Leading technology university.",
  "logoPath": "/images/mit_logo.png"
}

```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Registration successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "user": {
    "id": 1,
    "email": "admin@mit.edu",
    "name": "MIT"
  }
}
```

</details>

------------------------------------------------

### 4. Student Registration

- **Endpoint**: `/register/student`
- **Method**: `POST`
- **Description**: Registration of a student.

#### Request Parameters

- **Body (JSON)**:
  - `email` (string, required): Email of the student.
  - `password` (string, required): Password for the student.
  - `firstName` (string, required): First name of the student.
  - `lastName` (string, required): Last name of the student.
  - `phoneNumber` (string, required): Phone number of the student.
  - `profilePicturePath` (string, optional): Path to the student's profile picture.
  - `location` (string, required): Location of the student.
  - `degreeProgram` (string, required): Degree program the student is enrolled in.
  - `GPA` (float, optional): GPA of the student.
  - `graduationYear` (integer, optional): Graduation year of the student.
  - `CVpath` (string, required): Path to the student's CV.
  - `skills` (string, required): Skills of the student.
  - `languageSpoken` (string, required): Languages spoken by the student.
  - `university` (integer, required): ID of the university the student is associated with.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (string): Success message.
    - `token` (string): JWT token for authentication.
    - `user` (object): Registered user details.
      - `id` (integer): User ID.
      - `mail` (integer): User mail.
      - `firstName` (integer): User's first name.
      - `lastName` (integer): User's last name.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (string): Type of the error(`invalid_request` or `conflict`).
    - `message` (string): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (string): Type of error (`server_error`).
    - `message` (string): Error message.
    
<details>
<summary>Example Request</summary>

```json
POST /register/student
{
  "email": "student@mit.edu",
  "password": "securepassword",
  "firstName": "Alice",
  "lastName": "Smith",
  "phoneNumber": "1234567890",
  "profilePicturePath": "/images/alice.png",
  "location": "Cambridge, MA",
  "degreeProgram": "Computer Science",
  "GPA": 3.8,
  "graduationYear": 2025,
  "CVpath": "/cvs/alice_smith.pdf",
  "skills": "Python, Machine Learning",
  "languageSpoken": "English, Spanish",
  "university": 1
}

```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Registration successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "user": {
    "id": 1,
    "email": "student@mit.edu",
    "firstName": "Alice",
    "lastName": "Smith"
  }
}
```

</details>