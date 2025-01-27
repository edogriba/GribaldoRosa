# S&C Analysis API Specification

## Table of Contents

- [S&C Analysis API Specification](#sc-analysis-api-specification)
  - [Table of Contents](#table-of-contents)
  - [Endpoints](#endpoints)
    - [1. Get universities List](#1-get-universities-list)
      - [Response](#response)
    - [2. University Registration](#2-university-registration)
      - [Request Parameters](#request-parameters)
      - [Response](#response-1)
    - [3. Student Registration](#3-student-registration)
      - [Request Parameters](#request-parameters-1)
      - [Response](#response-2)
    - [4. Company Registration](#4-company-registration)
      - [Request Parameters](#request-parameters-2)
      - [Response](#response-3)
    - [5. User Login](#5-user-login)
      - [Request Parameters](#request-parameters-3)
      - [Response](#response-4)
    - [6. User Logout](#6-user-logout)
      - [Request Parameters](#request-parameters-4)
      - [Response](#response-5)
    - [7. Protected Endpoint](#7-protected-endpoint)
      - [Response](#response-6)
    - [8. Post Internship Position](#8-post-internship-position)
      - [Request Parameters](#request-parameters-5)
      - [Response](#response-7)
    - [9. Get Internship Position by ID](#9-get-internship-position-by-id)
      - [Request Parameters](#request-parameters-6)
      - [Response](#response-8)
    - [10. Get Internship Positions by Company](#10-get-internship-positions-by-company)
      - [Request Parameters](#request-parameters-7)
      - [Response](#response-9)
    - [11. Close Internship Position](#11-close-internship-position)
      - [Request Parameters](#request-parameters-8)
      - [Response](#response-10)
    - [12. Create Application](#12-create-application)
      - [Request Parameters](#request-parameters-9)
      - [Response](#response-11)
    - [13. Accept Application](#13-accept-application)
      - [Request Parameters](#request-parameters-10)
      - [Response](#response-12)
    - [14. Reject Application](#14-reject-application)
      - [Request Parameters](#request-parameters-11)
      - [Response](#response-13)
    - [15. Confirm Application](#15-confirm-application)
      - [Request Parameters](#request-parameters-12)
      - [Response](#response-14)
    - [16. Refuse Application](#16-refuse-application)
      - [Request Parameters](#request-parameters-13)
      - [Response](#response-15)

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
    - `message` (str): Registration successful.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'university'_)
      - `name` (str)
      - `address` (str)
      - `websiteURL` (str)
      - `description` (str)
      - `logoPath` (str)
    - `access_token` (str): JWT token for authentication.

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
  "user": {
    "id": 1,
    "email": "admin@mit.edu",
    "type": "university",
    "name": "MIT",
    "address": "Cambridge, MA",
    "websiteURL": "https://www.mit.edu/",
    "description": "Leading technology university.",
    "logoPath": "/images/mit_logo.png"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```

</details>

------------------------------------------------

### 3. Student Registration

- **Endpoint**: `/api/register/student`
- **Method**: `POST`
- **Description**: Registers a new student with required details.

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
    - `message` (str): Registration successful.
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
    - `access_token` (str): JWT token for authentication.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request` or `conflict`).
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
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```

</details>

------------------------------------------------

### 4. Company Registration

- **Endpoint**: `/api/register/company`
- **Method**: `POST`
- **Description**: Registers a new company with required details.

#### Request Parameters

- **Body (JSON)**:
  - `email` (str, required): Email of the company.
  - `password` (str, required): Password for the company.
  - `companyName` (str, required): Name of the company.
  - `logoPath` (str, optional): Path to the company's logo.
  - `description` (str, required): Description of the company.
  - `location` (str, required): Location of the company.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Registration successful.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str)
      - `description` (str)
      - `location` (str)
    - `access_token` (str): JWT token for authentication.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request` or `conflict`).
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
  "user": {
    "id": 1,
    "email": "company@xyz.com",
    "type": "company",
    "companyName": "XYZ Corporation",
    "logoPath": "/images/xyz_logo.png",
    "description": "Leading software solutions provider.",
    "location": "New York, NY"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
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
    - `access_token` (str): JWT token for authentication.

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
    - `access_token` (str): JWT token for authentication.

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
    - `access_token` (str): JWT token for authentication.

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
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
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
    "description": "Leading software solutions provider."
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
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
    "logoPath": "/images/mit_logo.png"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```

</details>

------------------------------------------------

### 6. User Logout

- **Endpoint**: `/api/userlogout`
- **Method**: `POST`
- **Description**: Logs out the authenticated user.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

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
Headers: {
  "Authorization": "Bearer <access_token>"
}
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

### 7. Protected Endpoint

- **Endpoint**: `/api/protected`
- **Method**: `GET`
- **Description**: Retrieves the current authenticated user's details.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `user` (dict): Authenticated user details.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`unauthorized`).
    - `message` (str): Error message, such as "Missing or invalid token."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
GET /api/protected
Headers: {
  "Authorization": "Bearer <access_token>"
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "type": "student",
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "1234567890",
    "profilePicture": "/images/john_doe.png",
    "location": "Cambridge, MA",
    "universityId": 1,
    "degreeProgram": "Computer Science",
    "GPA": 3.9,
    "graduationYear": 2024,
    "skills": "Python, Data Science",
    "CV": "/cvs/john_doe.pdf",
    "languageSpoken": "English, French"
  }
}
```

</details>

------------------------------------------------

### 8. Post Internship Position

- **Endpoint**: `/api/internship/post`
- **Method**: `POST`
- **Description**: Posts a new internship position with required details.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `companyId` (int, required): The ID of the company.
  - `programName` (str, required): The name of the program.
  - `duration` (str, required): The duration of the internship.
  - `location` (str, required): The location of the internship.
  - `roleTitle` (str, required): The title of the role.
  - `skillsRequired` (str, required): The skills required for the internship.
  - `compensation` (str, required): The compensation for the internship.
  - `benefits` (str, required): The benefits of the internship.
  - `languagesRequired` (str, required): The languages required for the internship.
  - `description` (str, required): The description of the internship.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Internship position posted successfully.
    - `internship_position` (dict): Posted internship details.
      - `id` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (str)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (str)
      - `benefits` (str)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/post
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "companyId": 1,
  "programName": "Summer Internship",
  "duration": "3 months",
  "location": "New York, NY",
  "roleTitle": "Software Engineer Intern",
  "skillsRequired": "Python, JavaScript",
  "compensation": "$3000/month",
  "benefits": "Health insurance, Gym membership",
  "languagesRequired": "English",
  "description": "An exciting opportunity to work with our software development team."
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Internship position posted successfully",
  "internship_position": {
    "id": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  }
}
```

</details>

------------------------------------------------

### 9. Get Internship Position by ID

- **Endpoint**: `/api/internship/get_by_id`
- **Method**: `POST`
- **Description**: Retrieves the details of an internship position by its ID.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `internship_position` (dict): Internship position details.
      - `internshipPositionId` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (str)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (str)
      - `benefits` (str)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message.

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`not_found`).
    - `message` (str): Error message, such as "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/get_by_id
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "internship_position": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  }
}
```

</details>

------------------------------------------------

### 10. Get Internship Positions by Company

- **Endpoint**: `/api/internship/get_by_company`
- **Method**: `POST`
- **Description**: Retrieves all internship positions posted by a specific company.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `companyId` (int, required): The ID of the company.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `internship_positions` (list): List of internship positions.
      - `id` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (str)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (str)
      - `benefits` (str)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message.

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`not_found`).
    - `message` (str): Error message, such as "No internships found for the given company ID."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/get_by_company
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "companyId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "internship_positions": [
    {
      "internshipPositionId": 1,
      "companyId": 1,
      "programName": "Summer Internship",
      "duration": "3 months",
      "location": "New York, NY",
      "roleTitle": "Software Engineer Intern",
      "skillsRequired": "Python, JavaScript",
      "compensation": "$3000/month",
      "benefits": "Health insurance, Gym membership",
      "languagesRequired": "English",
      "description": "An exciting opportunity to work with our software development team.",
      "status": "open"
    },
    {
      "internshipPositionId": 2,
      "companyId": 1,
      "programName": "Winter Internship",
      "duration": "2 months",
      "location": "San Francisco, CA",
      "roleTitle": "Data Analyst Intern",
      "skillsRequired": "SQL, Python",
      "compensation": "$2500/month",
      "benefits": "Health insurance, Gym membership",
      "languagesRequired": "English",
      "description": "An exciting opportunity to work with our data analysis team.",
      "status": "closed"
    }
  ]
}
```

</details>

------------------------------------------------

### 11. Close Internship Position

- **Endpoint**: `/api/internship/close`
- **Method**: `POST`
- **Description**: Closes an existing internship position.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipPositionId` (int, required): The ID of the internship position to be closed.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the internship position has been closed.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message.

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`not_found`).
    - `message` (str): Error message, such as "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/close
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Internship position closed successfully"
}
```

</details>

------------------------------------------------

### 12. Create Application

- **Endpoint**: `/api/application/create`
- **Method**: `POST`
- **Description**: Creates a new application for an internship position.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipPositionId` (int, required): The ID of the internship position to apply for.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `message` (str): Application created successfully.
    - `application` (dict): Created application details.
      - `applicationId` (int)
      - `internshipPositionId` (int)
      - `studentId` (int)
      - `status` (str)
    - `internshipPosition` (dict): Internship position details.
      - `internshipPositionId` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (str)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (str)
      - `benefits` (str)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)
    - `company` (dict): Company details.
      - `userId` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str)
      - `description` (str)
      - `location` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/create
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Application created successfully",
  "application": {
    "applicationId": 1,
    "internshipPositionId": 1,
    "studentId": 1,
    "status": "pending"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  },
  "company": {
    "userId": 1,
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


### 13. Accept Application

- **Endpoint**: `/api/application/accept`
- **Method**: `POST`
- **Description**: Accepts an application.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `applicationId` (int, required): The ID of the application to be accepted.
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the application has been accepted.
    - `application` (dict): Accepted application details.
    - `internshipPosition` (dict): Internship position details.
    - `student` (dict): Student details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message, such as "Invalid application Id." or "Invalid internship position Id." or "Invalid application state."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`unauthorized`).
    - `message` (str): Error message, such as "Only the company that posted the internship can accept applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/accept
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "applicationId": 1,
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Application accepted successfully",
  "application": {
    "applicationId": 1,
    "internshipPositionId": 1,
    "studentId": 1,
    "status": "accepted"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  },
  "student": {
    "id": 1,
    "email": "student@mit.edu",
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

### 14. Reject Application

- **Endpoint**: `/api/application/reject`
- **Method**: `POST`
- **Description**: Rejects an application.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `applicationId` (int, required): The ID of the application to be rejected.
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the application has been rejected.
    - `application` (dict): Rejected application details.
    - `internshipPosition` (dict): Internship position details.
    - `student` (dict): Student details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message, such as "Invalid application Id." or "Invalid internship position Id." or "Invalid application state."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`unauthorized`).
    - `message` (str): Error message, such as "Only the company that posted the internship can reject applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/reject
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "applicationId": 1,
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Application rejected successfully",
  "application": {
    "applicationId": 1,
    "internshipPositionId": 1,
    "studentId": 1,
    "status": "rejected"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  },
  "student": {
    "id": 1,
    "email": "student@mit.edu",
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

### 15. Confirm Application

- **Endpoint**: `/api/application/confirm`
- **Method**: `POST`
- **Description**: Confirms an application.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `applicationId` (int, required): The ID of the application to be confirmed.
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the application has been confirmed.
    - `application` (dict): Confirmed application details.
    - `internshipPosition` (dict): Internship position details.
    - `company` (dict): Company details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message, such as "Invalid application Id." or "Invalid internship position Id." or "Invalid application state."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`unauthorized`).
    - `message` (str): Error message, such as "Only the student that applied can confirm applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/confirm
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "applicationId": 1,
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Application confirmed successfully",
  "application": {
    "applicationId": 1,
    "internshipPositionId": 1,
    "studentId": 1,
    "status": "confirmed"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  },
  "company": {
    "userId": 1,
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

### 16. Refuse Application

- **Endpoint**: `/api/application/refuse`
- **Method**: `POST`
- **Description**: Refuses an application.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `applicationId` (int, required): The ID of the application to be refused.
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `message` (str): Success message indicating the application has been refused.
    - `application` (dict): Refused application details.
    - `internshipPosition` (dict): Internship position details.
    - `company` (dict): Company details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): Type of the error (`invalid_request`).
    - `message` (str): Error message, such as "Invalid application Id." or "Invalid internship position Id." or "Invalid application state."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`unauthorized`).
    - `message` (str): Error message, such as "Only the student that applied can refuse applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): Type of error (`server_error`).
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/refuse
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "applicationId": 1,
  "internshipPositionId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "message": "Application refused successfully",
  "application": {
    "applicationId": 1,
    "internshipPositionId": 1,
    "studentId": 1,
    "status": "refused"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": "3 months",
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": "$3000/month",
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "open"
  },
  "company": {
    "userId": 1,
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

