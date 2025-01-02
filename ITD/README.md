# S&C Steps to Clone and Run the Project

## Clone the Repository

Open a terminal.

Navigate to the folder where you want to clone the project.

Run the following command:

```bash
git clone https://github.com/edogriba/GribaldoRosa.git
```

Navigate into the project folder:

```bash
cd GribaldoRosa/ITD
```

## Setup the Frontend (React)

### Prerequisites

Before proceeding, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v20 or higher)
- [npm](https://www.npmjs.com/)
- [Git](https://git-scm.com/)


### Installation and Setup

1. **Navigate to the frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   npm install @mui/material @emotion/react @emotion/styled @mui/styled-engine-sc styled-components
   npm install react-router-dom
   ```

### Start the development server

```bash
npm start dev
```

The React app should now be running at [http://localhost:3000/](http://localhost:3000/).

<!--    NON SO SE NECESSARIO O NO

### Environment Variables for Frontend

Environment variables for the frontend should be defined in a `.env` file at the root of the frontend folder. Currently only this following environment variable is used:

- `REACT_APP_BACKEND_URL`: The URL of the backend API (e.g. http://localhost:3000/ for local development)

Restart the development server if it was running.
-->

## Setup the Backend (Flask)

### Prerequisites

- [Python](https://www.python.org/) (version 3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/) (comes pre-installed with Python)

### Installation and Setup

1. **Navigate to the backend directory**

   ```bash
   cd ../backend
   ```

2. **Set Up Virtual Environment**

   (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   ```
   or

   ```bash
   python3 -m venv venv
   ```
   Activate the virtual environment:

   - On **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```powershell
     venv\Scripts\activate
     ```

3. **Install dependencies**

   Once the virtual environment is active, install the required dependencies using `pip`:
   
   ```bash
    pip install update
    pip install --upgrade pip
    pip install -r requirements.txt
   ```

## Start the Development Server

Start the Flask server:

```bash
python run.py
```
The Flask backend should now be running at http://127.0.0.1:5000/.

## Notes

Ensure the frontend is configured to communicate with the backend (e.g., via environment variables or configuration files).

If you encounter any issues, check the logs or consult the project documentation.

## Structure

The project is structured as follows:

- `backend/`        : Flask API
  - `app/`                : Flask App
    - `api.md`                  :
    - `routes.py`               :
  - `requirements.txt`    : Requirements
  - `.env`                : Backend environment
  - `run.py`              : To run the project
  - `SC.db`               : Database SQLite
- `frontend/`       : React application
  - `public/`             : Static files that are served as-is
  - `src/`                : Source files
    - `api/`                    : API interface
    - `assets/`                 : Assets such as images, styles, etc.
    - `components/`             : Reusable components
    - `hooks/`                  : Share logic between components
    - `pages/`                  : Pages
    - `util/`                   : Utility functions and helpers
    - `.env`                    : Frontend environment
- `README.md`       : This file
