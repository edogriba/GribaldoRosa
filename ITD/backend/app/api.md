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
    - [17. Get Application by ID](#17-get-application-by-id)
      - [Request Parameters](#request-parameters-14)
      - [Response](#response-16)
    - [18. Get Applications by Student](#18-get-applications-by-student)
      - [Request Parameters](#request-parameters-15)
      - [Response](#response-17)
    - [19. Get Applications by Internship Position](#19-get-applications-by-internship-position)
      - [Request Parameters](#request-parameters-16)
      - [Response](#response-18)
    - [20. Get Internship Previews by Company](#20-get-internship-previews-by-company)
      - [Request Parameters](#request-parameters-17)
      - [Response](#response-19)
    - [21. Get Internship Previews by Student](#21-get-internship-previews-by-student)
      - [Request Parameters](#request-parameters-18)
      - [Response](#response-20)
    - [22. Get Internship Previews by University](#22-get-internship-previews-by-university)
      - [Request Parameters](#request-parameters-19)
      - [Response](#response-21)
    - [23. Get Full Internship Data by ID](#23-get-full-internship-data-by-id)
      - [Request Parameters](#request-parameters-20)
      - [Response](#response-22)
    - [24. Finish Internship](#24-finish-internship)
      - [Request Parameters](#request-parameters-21)
      - [Response](#response-23)
    - [25. Get Search Filters](#25-get-search-filters)
      - [Response](#response-24)
    - [26. Search Internship Positions with Filters](#26-search-internship-positions-with-filters)
      - [Request Parameters](#request-parameters-22)
      - [Response](#response-25)
    - [27. Search Internship Positions without Filters](#27-search-internship-positions-without-filters)
      - [Response](#response-26)

## Endpoints

### 1. Get universities List

- **Endpoint**: `/api/universitylist`
- **Method**: `GET`
- **Description**: Retrieves a list of universities with their IDs and names.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Universities retrieved"
    - `universities` (list): List of universities.
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
    - `type` (str): `created`
    - `message` (str): Registration successful.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'university'_)
      - `name` (str)
      - `address` (str)
      - `websiteURL` (str)
      - `description` (str)
      - `logoPath` (str | None)
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
  "type": "created",
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
    - `type` (str): `created`
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
    - `type` (str): `server_error`
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
  "type": "created",
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
    - `type` (str): `created`
    - `message` (str): Registration successful.
    - `user` (dict): Registered user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str | None)
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
  "type": "created",
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
    - `type` (str): `success`
    - `message` (str): Login successful.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'student'_)
      - `firstName` (str)
      - `lastName` (str)
      - `phoneNumber` (str)
      - `profilePicture` (str | None)
      - `location` (str)
      - `universityId` (int)        
      - `degreeProgram` (str)
      - `GPA` (float | None)
      - `graduationYear` (int | None)
      - `skills` (str)
      - `CV` (str)
      - `languageSpoken` (str)
    - `access_token` (str): JWT token for authentication.

  - **Body (JSON) [Company]**:
    - `type` (str): `success`
    - `message` (str): Login successful.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'company'_)
      - `companyName` (str)
      - `logoPath` (str | None)
      - `description` (str)
      - `location` (str)
    - `access_token` (str): JWT token for authentication.

  - **Body (JSON) [University]**:
    - `type` (str): `success`
    - `message` (str): Login successful.
    - `user` (dict): Logged-in user details.
      - `id` (int)
      - `email` (str)
      - `type` (str): User type (_'university'_)
      - `name` (str)
      - `address` (str)
      - `websiteURL` (str)
      - `description` (str)
      - `logoPath` (str | None)
    - `access_token` (str): JWT token for authentication.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as "Email and password are required."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `invalid_credentials`
    - `message` (str): Error message, such as "Invalid email or password."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
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
  "type": "success",
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
  "type": "success",
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
    - `type` (str): `success`
    - `message` (str): Success message indicating the user has been logged out.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
    - `type` (str): `success`
    - `message` (str): "Access granted."
    - `user` (dict): Authenticated user details.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Missing or invalid token."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Access granted",
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

- **Endpoint**: `/api/internship_position/post`
- **Method**: `POST`
- **Description**: Posts a new internship position with required details.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `companyId` (int, required): The ID of the company.
  - `programName` (str, required): The name of the program.
  - `duration` (int, required): The duration of the internship.
  - `location` (str, required): The location of the internship.
  - `roleTitle` (str, required): The title of the role.
  - `skillsRequired` (str, required): The skills required for the internship.
  - `compensation` (int, optional): The compensation for the internship.
  - `benefits` (str, optional): The benefits of the internship.
  - `languagesRequired` (str, required): The languages required for the internship.
  - `description` (str, required): The description of the internship.

#### Response

- **201 Created**:
  - **Body (JSON)**:
    - `type` (str): `created`
    - `message` (str): Internship position posted successfully.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "Only companies can post internships."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "duration": 3,
  "location": "New York, NY",
  "roleTitle": "Software Engineer Intern",
  "skillsRequired": "Python, JavaScript",
  "compensation": 3000,
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
  "type": "created",
  "message": "Internship position posted successfully",
}
```

</details>

------------------------------------------------

### 9. Get Internship Position by ID

- **Endpoint**: `/api/internship_position/get_by_id`
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
    - `type` (str): `success`
    - `message` (str): "Internship position retrieved successfully."
    - `internship_position` (dict): Internship position details.
      - `internshipPositionId` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (int)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (int | None)
      - `benefits` (str | None)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Internship position retrieved successfully.",
  "internship_position": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": 3,
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": 3000,
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

- **Endpoint**: `/api/internship_position/get_by_company`
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
    - `type` (str): `success`
    - `message` (str): "Internship positions retrieved successfully."
    - `internship_positions` (list): List of internship positions.
      - `internshipPositionId` (int)
      - `companyId` (int)
      - `programName` (str)
      - `duration` (int)
      - `location` (str)
      - `roleTitle` (str)
      - `skillsRequired` (str)
      - `compensation` (int | None)
      - `benefits` (str | None)
      - `languagesRequired` (str)
      - `description` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): "Invalid company ID."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "No internships found for the given company ID."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Internship positions retrieved successfully.",
  "internship_positions": [
    {
      "internshipPositionId": 1,
      "companyId": 1,
      "programName": "Summer Internship",
      "duration": 3,
      "location": "New York, NY",
      "roleTitle": "Software Engineer Intern",
      "skillsRequired": "Python, JavaScript",
      "compensation": 3000,
      "benefits": "Health insurance, Gym membership",
      "languagesRequired": "English",
      "description": "An exciting opportunity to work with our software development team.",
      "status": "open"
    },
    {
      "internshipPositionId": 2,
      "companyId": 1,
      "programName": "Winter Internship",
      "duration": 2,
      "location": "San Francisco, CA",
      "roleTitle": "Data Analyst Intern",
      "skillsRequired": "SQL, Python",
      "compensation": 2500,
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

- **Endpoint**: `/api/internship_position/close`
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
    - `type` (str): `success`
    - `message` (str): "Internship position closed successfully."
- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): "Invalid internship ID."
  
- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "Only companies can close internships." or "You are not authorized to close this internship."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
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
    - `type` (str): `created`
    - `message` (str): "Application created successfully."

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as:
      - "Invalid internship position Id."
      - "Internship position is closed." 
      - "Invalid application data."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Only students can create applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type" : "created",
  "message": "Application created successfully"
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
    - `type` (str): `success`
    - `message` (str): "Application accepted successfully."

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as:
      - "Invalid application Id." 
      - "Invalid internship position Id." 
      - "Invalid application status."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Only the company that posted the internship can accept applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Application accepted successfully",
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
    - `type` (str): `success`
    - `message` (str): "Application rejected successfully."

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as:
      - "Invalid application Id." 
      - "Invalid internship position Id." 
      - "Invalid application status."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Only the company that posted the internship can reject applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Application rejected successfully"
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
    - `type` (str): `success`
    - `message` (str): "Application confirmed successfully."

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as:
      - "Invalid application Id." 
      - "Invalid internship position Id." 
      - "Invalid application status."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Only the student that applied can confirm applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Application confirmed successfully",
}
```

</details>

------------------------------------------------

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
    - `type` (str): `success`
    - `message` (str): Success message indicating the application has been refused.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as 
      - "Invalid application Id." 
      - "Invalid internship position Id." 
      - "Invalid application status."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "Only the student that applied can refuse applications."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Application refused successfully",
}
```

</details>

------------------------------------------------

### 17. Get Application by ID

- **Endpoint**: `/api/application/get_by_id`
- **Method**: `POST`
- **Description**: Retrieves the details of an application by its ID.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `applicationId` (int, required): The ID of the application.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `application` (dict): Application details.
    - `internshipPosition` (dict): Internship position details.
    - `student` (dict): Student details.
    - `company` (dict): Company details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "You can only view your own applications."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as:
      - "Application not found."
      - "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/get_by_id
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "applicationId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
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
  },
  "company": {
    "id": 1,
    "email": "company@xyz.com",
    "companyName": "XYZ Corporation",
    "logoPath": "/images/xyz_logo.png",
    "description": "Leading software solutions provider.",
    "location": "New York, NY"
  }
}
```

</details>

------------------------------------------------

### 18. Get Applications by Student

- **Endpoint**: `/api/application/get_by_student`
- **Method**: `POST`
- **Description**: Retrieves all applications made by a specific student.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `studentId` (int, required): The ID of the student.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Applications found successfully."
    - `applications` (list): List of applications with details.
      - `application` (dict): Application details.
      - `internship` (dict): Internship position details.
      - `company` (dict): Company details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "You can only view your own applications."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Applications not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/get_by_student
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "studentId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Applications found successfully",
  "applications": [
    {
      "application": {
        "applicationId": 1,
        "internshipPositionId": 1,
        "studentId": 1,
        "status": "pending"
      },
      "internship": {
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
        "id": 1,
        "email": "company@xyz.com",
        "companyName": "XYZ Corporation",
        "logoPath": "/images/xyz_logo.png",
        "description": "Leading software solutions provider.",
        "location": "New York, NY"
      }
    }
  ]
}
```

</details>

------------------------------------------------

### 19. Get Applications by Internship Position

- **Endpoint**: `/api/application/get_by_internship_position`
- **Method**: `POST`
- **Description**: Retrieves all applications for a specific internship position.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Applications found successfully."
    - `applications` (list): List of applications with details.
      - `application` (dict): Application details.
      - `student` (dict): Student details.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): Error message, such as "You can only view applications for your own internship positions."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Applications not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/application/get_by_internship_position
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
  "type": "success",
  "message": "Applications found successfully",
  "applications": [
    {
      "application": {
        "applicationId": 1,
        "internshipPositionId": 1,
        "studentId": 1,
        "status": "pending"
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
  ]
}
```

</details>

------------------------------------------------

### 20. Get Internship Previews by Company

- **Endpoint**: `/api/internship/get_by_company`
- **Method**: `POST`
- **Description**: Retrieves a preview of all internship positions posted by a specific company.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `companyId` (int, required): The ID of the company.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internships retrieved successfully."
    - `internshipsPreview` (list): List of internship previews.
      - `student_name` (str)
      - `student_photoPath` (str | None)
      - `internshipId` (int)
      - `roleTitle` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): "Invalid company ID."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "You are not authorized to view internships posted by this company."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): "No internship previews found for the given company ID."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
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
  "type": "success",
  "message": "Internships retrieved successfully.",
  "internshipsPreview": [
    {
      "student_name": "Alice Smith",
      "student_photoPath": "/images/alice.png",
      "internshipId": 1,
      "roleTitle": "Software Engineer Intern",
      "status": "open"
    },
    {
      "student_name": "Bob Johnson",
      "student_photoPath": "/images/bob.png",
      "internshipId": 2,
      "roleTitle": "Data Analyst Intern",
      "status": "closed"
    }
  ]
}
```

</details>

------------------------------------------------

### 21. Get Internship Previews by Student

- **Endpoint**: `/api/internship/get_by_student`
- **Method**: `POST`
- **Description**: Retrieves a preview of all internship positions applied for by a specific student.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `studentId` (int, required): The ID of the student.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internships retrieved successfully."
    - `internshipsPreview` (list): List of internship previews.
      - `company_name` (str)
      - `company_photoPath` (str | None)
      - `internshipId` (int)
      - `roleTitle` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): "Invalid student ID."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "You are not authorized to view internships for this student."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): "No internship previews found for the given student ID."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/get_by_student
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "studentId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Internships retrieved successfully.",
  "internshipsPreview": [
    {
      "company_name": "XYZ Corporation",
      "company_photoPath": "/images/xyz_logo.png",
      "internshipId": 1,
      "roleTitle": "Software Engineer Intern",
      "status": "open"
    },
    {
      "company_name": "ABC Inc.",
      "company_photoPath": "/images/abc_logo.png",
      "internshipId": 2,
      "roleTitle": "Data Analyst Intern",
      "status": "closed"
    }
  ]
}
```

</details>

------------------------------------------------

### 22. Get Internship Previews by University

- **Endpoint**: `/api/internship/get_by_university`
- **Method**: `POST`
- **Description**: Retrieves a preview of all internship positions associated with a specific university.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `universityId` (int, required): The ID of the university.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internships retrieved successfully."
    - `internshipsPreview` (list): List of internship previews.
      - `student_name` (str)
      - `company_name` (str)
      - `internshipId` (int)
      - `roleTitle` (str)
      - `status` (str)

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): "Invalid university ID."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "You are not authorized to view internships for this university."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): "No internship previews found for the given university ID."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/get_by_university
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "universityId": 1
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Internships retrieved successfully.",
  "internshipsPreview": [
    {
      "student_name": "Alice Smith",
      "company_name": "XYZ Corporation",
      "internshipId": 1,
      "roleTitle": "Software Engineer Intern",
      "status": "open"
    },
    {
      "student_name": "Bob Johnson",
      "company_name": "ABC Inc.",
      "internshipId": 2,
      "roleTitle": "Data Analyst Intern",
      "status": "closed"
    }
  ]
}
```

</details>

------------------------------------------------

### 23. Get Full Internship Data by ID

- **Endpoint**: `/api/internship/get_by_id`
- **Method**: `POST`
- **Description**: Retrieves the full details of an internship position by its ID.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipPositionId` (int, required): The ID of the internship position.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internship position retrieved successfully."
    - `internship` (dict): Internship details.
    - `internshipPosition` (dict): Internship position details.
    - `application` (dict): Application details.
    - `student` (dict): Student details.
    - `company` (dict): Company details.


- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message.

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Internship position not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.
// ERRORE??
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
  "type": "success",
  "message": "Internship position retrieved successfully.",
  "internship": {
    "internshipId": 3,
    "internshipPositionId": 1,
    "applicationId": 2,
    "status": "Ongoing"
  },
  "internshipPosition": {
    "internshipPositionId": 1,
    "companyId": 1,
    "programName": "Summer Internship",
    "duration": 3,
    "location": "New York, NY",
    "roleTitle": "Software Engineer Intern",
    "skillsRequired": "Python, JavaScript",
    "compensation": 4000,
    "benefits": "Health insurance, Gym membership",
    "languagesRequired": "English",
    "description": "An exciting opportunity to work with our software development team.",
    "status": "Open"
  },
  "application": {
    "applicationId": 1,
    "studentId": 1,
    "internshipPositionId": 1,
    "status": "Pending"
  },
  "student": {
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
  "company": {
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

### 24. Finish Internship

- **Endpoint**: `/api/internship/finish`
- **Method**: `POST`
- **Description**: Marks an internship as finished.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `internshipId` (int, required): The ID of the internship.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internship finished successfully."

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as "Invalid internship ID." or "Invalid student ID."

- **401 Unauthorized**:
  - **Body (JSON)**:
    - `type` (str): `unauthorized`
    - `message` (str): "You are not authorized to finish this internship."

- **404 Not Found**:
  - **Body (JSON)**:
    - `type` (str): `not_found`
    - `message` (str): Error message, such as "Internship not found."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/internship/finish
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "internshipId": 1,
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Internship finished successfully"
}
```

</details>

------------------------------------------------

### 25. Get Search Filters

- **Endpoint**: `/api/search/filters`
- **Method**: `GET`
- **Description**: Retrieves search filters for internship positions.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Search filters found successfully."
    - `roleTitles` (list): List of role titles.
    - `locations` (list): List of locations.
    - `companiesNames` (list): List of company names.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
GET /api/search/filters
Headers: {
  "Authorization": "Bearer <access_token>"
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Search filters found successfully",
  "roleTitles": ["Software Engineer Intern", "Data Analyst Intern"],
  "locations": ["New York, NY", "San Francisco, CA"],
  "companiesNames": ["XYZ Corporation", "ABC Inc."]
}
```

</details>

------------------------------------------------

### 26. Search Internship Positions with Filters

- **Endpoint**: `/api/search_with_filters`
- **Method**: `POST`
- **Description**: Searches for internship positions based on provided filters.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

- **Body (JSON)**:
  - `roleTitle` (str, optional): The title of the role.
  - `location` (str, optional): The location of the internship.
  - `companyName` (str, optional): The name of the company.
  - `minStipend` (int, optional): The minimum stipend for the internship.
  - `minDuration` (int, optional): The minimum duration of the internship.
  - `maxDuration` (int, optional): The maximum duration of the internship.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internships found successfully."
    - `internships` (list): List of internships matching the filters.

- **400 Bad Request**:
  - **Body (JSON)**:
    - `type` (str): `invalid_request`
    - `message` (str): Error message, such as "Invalid role title." or "Invalid location."

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
POST /api/search_with_filters
Headers: {
  "Authorization": "Bearer <access_token>"
}
{
  "roleTitle": "Software Engineer Intern",
  "location": "New York, NY",
  "companyName": "XYZ Corporation",
  "minStipend": 3000,
  "minDuration": 3,
  "maxDuration": 6
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Internships found successfully",
  "internships": [
    {
      "internshipPositionId": 1,
      "companyId": 1,
      "programName": "Summer Internship",
      "duration": 3,
      "location": "New York, NY",
      "roleTitle": "Software Engineer Intern",
      "skillsRequired": "Python, JavaScript",
      "compensation": 3000,
      "benefits": "Health insurance, Gym membership",
      "languagesRequired": "English",
      "description": "An exciting opportunity to work with our software development team.",
      "status": "open"
    }
  ]
}
```

</details>

------------------------------------------------

### 27. Search Internship Positions without Filters

- **Endpoint**: `/api/search_without_filters`
- **Method**: `GET`
- **Description**: Retrieves all internship positions without any filters.

#### Request Parameters

- **Headers**:
  - `Authorization` (str, required): Bearer token for authentication.

#### Response

- **200 OK**:
  - **Body (JSON)**:
    - `type` (str): `success`
    - `message` (str): "Internships found successfully."
    - `internships` (list): List of all internships.

- **500 Internal Server Error**:
  - **Body (JSON)**:
    - `type` (str): `server_error`
    - `message` (str): Error message.

<details>
<summary>Example Request</summary>

```json
GET /api/search_without_filters
Headers: {
  "Authorization": "Bearer <access_token>"
}
```

</details>

<details>
<summary>Example Response</summary>

```json
{
  "type": "success",
  "message": "Internships found successfully",
  "internships": [
    {
      "internshipPositionId": 1,
      "companyId": 1,
      "programName": "Summer Internship",
      "duration": 3,
      "location": "New York, NY",
      "roleTitle": "Software Engineer Intern",
      "skillsRequired": "Python, JavaScript",
      "compensation": 3000,
      "benefits": "Health insurance, Gym membership",
      "languagesRequired": "English",
      "description": "An exciting opportunity to work with our software development team.",
      "status": "open"
    },
    {
      "internshipPositionId": 2,
      "companyId": 2,
      "programName": "Winter Internship",
      "duration": 2,
      "location": "San Francisco, CA",
      "roleTitle": "Data Analyst Intern",
      "skillsRequired": "SQL, Python",
      "compensation": 2500,
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
