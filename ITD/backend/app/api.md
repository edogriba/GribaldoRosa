# S&C Analysis API Specification

## Table of Contents

- [S&C Analysis API Specification](#s&c-analysis-api-specification)
  - [Table of Contents](#table-of-contents)
  - [Endpoints](#endpoints)
    - [1. Get universities List](#1-get-universities-list)
      - [Response](#response-1)
    - [2. University Registration](#2-university-registration)
      - [Request Parameters](#request-parameters-2)
      - [Response](#response-2)
    - [3. Student Registration](#3-student-registration)
      - [Request Parameters](#request-parameters-3)
      - [Response](#response-3)
    - [4. Company Registration](#4-company-registration)
      - [Request Parameters](#request-parameters-4)
      - [Response](#response-4)
    - [5. User Login](#5-user-login)
      - [Request Parameters](#request-parameters-5)
      - [Response](#response-5)
    - [6. User Logout](#6-user-logout)
      - [Response](#response-6)
    - [7. Refresh Token](#7-refresh-token)
      - [Request Parameters](#request-parameters-7)
      - [Response](#response-7)

## Endpoints

### 1. Get universities List

- **Endpoint**: `/api/universitylist`
- **Method**: `GET`
- **Description**: Retrieves a list of universities with their IDs and names.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `id` (int): ID of the university.
    - `name` (str): Name of the university.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`database_error`).
    - `message` (str): Error message.

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

### 2. University Registration

- **Endpoint**: `/api/register/university`
- **Method**: `POST`
- **Description**: Registers a new university with required details.

#### Request Parameters

- **Body (JSON)**:
  - `university_mail` (str, required): Email of the university.
  - `university_password` (str, required): Password of the university.
  - `name` (str, required): Name of the university.
  - `location` (str, required): Location of the university.
  - `websiteURL` (str, required): URL of the university's website.
  - `description` (str, required): Description of the university.
  - `logoPath` (str, optional): Path of the university's logo.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Success message.
    - `token` (str): JWT token for authentication.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'university'_)
      - `name` (str)
      - `address` (str)
      - `websiteURL` (str)
      - `description` (str)
      - `logoPath` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error(`invalid_request` or `conflict`).
    - `message` (str): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.
    
<details>
<summary>Example Request</summary>

```json
POST /api/register/university
{
  "university_email": "admin@mit.edu",
  "university_password": "securepassword",
  "name": "MIT",
  "location": "Cambridge, MA",
  "websiteURL": "https://www.mit.edu/",
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
    "type": "university",
    "name": "MIT",
    "address": "Cambridge, MA",
    "websiteURL": "https://www.mit.edu/",
    "description": "Leading technology university.",
    "logoPath": "/images/mit_logo.png"
  }
}
```

</details>

------------------------------------------------

### 3. Student Registration

- **Endpoint**: `/api/register/student`
- **Method**: `POST`
- **Description**: Registration of a student.

#### Request Parameters

- **Body (JSON)**:
  - `email` (str, required): Email of the student.
  - `password` (str, required): Password for the student.
  - `firstName` (str, required): First name of the student.
  - `lastName` (str, required): Last name of the student.
  - `phoneNumber` (str, required): Phone number of the student.
  - `profilePicturePath` (str, optional): Path to the student's profile picture.
  - `location` (str, required): Location of the student.
  - `degreeProgram` (str, required): Degree program the student is enrolled in.
  - `GPA` (float, optional): GPA of the student.
  - `graduationYear` (int, optional): Graduation year of the student.
  - `CVpath` (str, required): Path to the student's CV.
  - `skills` (str, required): Skills of the student.
  - `languageSpoken` (str, required): Languages spoken by the student.
  - `university` (int, required): ID of the university the student is associated with.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Success message.
    - `token` (str): JWT token for authentication.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'student'_)
      - `firstName` (str)
      - `lastName` (str)
      - `phoneNumber` (str)
      - `profilePicture` (str)
      - `location` (str)
      - `universityId` (int)        
      - `degreeProgram` (str)
      - `GPA` (float)
      - `graduationYear` (int)
      - `skills` (str)
      - `CV` (str)
      - `languageSpoken` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error(`invalid_request` or `conflict`).
    - `message` (str): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.
    
<details>
<summary>Example Request</summary>

```json
POST /api/register/student
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
    "type": "student",
    "firstName": "Alice",
    "lastName": "Smith",
    "phoneNumber": "1234567890",
    "profilePicture": "/images/alice.png",
    "location": "Cambridge, MA",
    "universityId": 1,
    "degreeProgram": "Computer Science",
    "GPA": 3.8,
    "graduationYear": 2025,
    "skills": "Python, Machine Learning",
    "CV": "/cvs/alice_smith.pdf",
    "languageSpoken": "English, Spanish"
  }
}
```

</details>

------------------------------------------------

### 4. Company Registration

- **Endpoint**: `/api/register/company`
- **Method**: `POST`
- **Description**: Registration of a company.

#### Request Parameters

- **Body (JSON)**:
  - `email` (str, required): Email of the student.
  - `password` (str, required): Password for the student.
  - `companyName` (str, required): Name of the company.
  - `logoPath` (str, optional): Path to the company's logo.
  - `description` (str, required): Description of the company.
  - `location` (str, required): Location of the company.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Success message.
    - `token` (str): JWT token for authentication.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str)
      - `description` (str)
      - `location` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error(`invalid_request` or `conflict`).
    - `message` (str): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.
    
<details>
<summary>Example Request</summary>

```json
POST /api/register/company
{
  "email": "company@xyz.com",
  "password": "securepassword",
  "companyName": "XYZ Corporation",
  "logoPath": "/images/xyz_logo.png",
  "description": "Leading software solutions provider.",
  "location": "New York, NY"
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
    "email": "company@xyz.com",
    "type": "company",
    "companyName": "XYZ Corporation",
    "logoPath": "/images/xyz_logo.png",
    "description": "Leading software solutions provider.",
    "location": "New York, NY"
  }
}
```

</details>

------------------------------------------------

### 5. User Login

- **Endpoint**: `/api/userlogin`
- **Method**: `POST`
- **Description**: Authenticates the user by verifying email and password.

#### Request Parameters

- **Body (JSON)**:
  - `email` (str, required): Email of the user.
  - `password` (str, required): Password of the user.

#### Response

- **200 OK**:
  - **Body (JSON) [Student]**:
    - `message` (str): Success message.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'student'_)
      - `firstName` (str)
      - `lastName` (str)
      - `phoneNumber` (str)
      - `profilePicture` (str)
      - `location` (str)
      - `universityId` (int)        
      - `degreeProgram` (str)
      - `GPA` (float)
      - `graduationYear` (int)
      - `skills` (str)
      - `CV` (str)
      - `languageSpoken` (str)

  - **Body (JSON) [Company]**:
    - `message` (str): Success message.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str)
      - `description` (str)
      - `location` (str)

  - **Body (JSON) [University]**:
    - `message` (str): Success message.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'university'_)
      - `name` (str)
      - `address` (str)
      - `websiteURL` (str)
      - `description` (str)
      - `logoPath` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (invalid_request).
    - `message` (str): Error message, such as "Email and password are required."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (invalid_credentials).
    - `message` (str): Error message, such as "Invalid email or password."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (server_error).
    - `message` (str): Error message.

<details> 
<summary>Example Request</summary>

```json
POST /api/userlogin
{
  "email": "student@mit.edu",
  "password": "securepassword"
}
```

</details> 

<details> 
<summary>Example Response</summary>

**For a student**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "email": "student@mit.edu",
    "type": "student",
    "firstName": "Alice",
    "lastName": "Smith",
    "phoneNumber": "1234567890",
    "profilePicture": "/images/alice.png",
    "location": "Cambridge, MA",
    "universityId": 1,
    "degreeProgram": "Computer Science",
    "GPA": 3.8,
    "graduationYear": 2025,
    "skills": "Python, Machine Learning",
    "CV": "/cvs/alice_smith.pdf",
    "languageSpoken": "English, Spanish"
  }
}
```

**For a company**
```json
{
  "message": "Login successful",
  "user": {
    "id": 2,
    "email": "company@xyz.com",
    "type": "company",
    "companyName": "XYZ Corporation",
    "location": "New York, NY",
    "logoPath": "/images/xyz_logo.png",
    "description": "Leading software solutions provider.",
  }
}
```

**For a university**
```json
{
  "message": "Login successful",
  "user": {
    "id": 3,
    "email": "university@mit.edu",
    "type": "university",
    "name": "MIT",
    "address": "Cambridge, MA",
    "websiteURL": "https://www.mit.edu",
    "description": "Leading technology university.",
    "logoPath": "/images/mit_logo.png",
  }
}
```

</details>

------------------------------------------------

### 6. User Logout

- **Endpoint**: `/api/userlogout`
- **Method**: `POST`
- **Description**: Logs out the authenticated user.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the user has been logged out.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/userlogout
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Logout successful"
}
```

</details>

------------------------------------------------

### 7. Refresh Token

- **Endpoint**: `/api/token/refresh`
- **Method**: `POST`
- **Description**: Refreshes the JWT access token using a refresh token.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token containing the refresh token.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message.
    - `access_token` (str): New JWT access token.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`invalid_token`).
    - `message` (str): Error message, such as "Unauthorized".

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/token/refresh
Headers: {
  "Authorization": "Bearer <refresh_token>"
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Token refreshed successfully",
  "access_token": "new_access_token"
}
```

</details>