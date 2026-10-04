# Student Management System
**A system used to manage students in an institution.**

## About
**This project is built for learning how Python can interact with MySQL**

## Features
- Add a student to a local MySQL database.
- View a particular student's details.
- View a particular student's marks.
- View the list of all students.
- Update a particular student's details.
- Update a particular student's marks.
- Delete a particular student from the database.

## Technologies Used
- Python
- MySQL
- MySQL Connector for Python

## How to use

### 1. Configure environment variables

**This project uses enviroment variables to store MySQL credentials instead of hardcoding them in the source code.**

**Set the required environment variables before running the application**

**Create a new environment variable as `MYSQL_PASSWORD`**

**Set its value as the password of your local MySQL server.**

### 2. MySQL configuration

**This application currently uses the following MySQL database configuration:**

- Database: `studentmanagement`
- Host: `localhost`
- Port : `3306`
- User : `root`
- Password : `<value of MYSQL_PASSWORD environment variable>`

### 3. Database setup

**Run `schema.py` in the config folder to create the required database and tables**

```bash
python config/schema.py
```

### 4. Install dependencies

**Install the required Python dependencies by running the following command:**

```bash
pip install -r requirements.txt
```

### 5. Run the application

**Run the application in the main folder by running the following command:**

```bash
python main/main.py
```

## Project structure
```text
Student_Management/
    |--config
        |--Branches.py
        |--database.py
        |--schema.py
        |--Subjects.py
    |--main
        |--main.py
    |--models
        |--student.py
    |--repositories
        |--StudentRepository.py
    |--services
        |--Student_Service.py
    |--README.md
    |--requirements.txt
```
## Architecture
- config/ -> Configuration of the database and its schema.
- main/ -> Handles user interaction.
- models/ -> Represents a student.
- repositories -> Handles MySQL operations.
- services/ -> Contains the business logic and data validation.