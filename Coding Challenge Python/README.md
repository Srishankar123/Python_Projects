# 💼 CareerHub – Python Coding Challenge Project

Welcome to the **CareerHub** repository! This project simulates a job application and career management platform developed using **Python** and **MS SQL Server**. Built as part of a coding challenge, CareerHub demonstrates modular programming, exception handling, and database interaction using the DAO pattern.

---

## 📁 Repository Structure

- `main.py` – Command-line interface for interacting with the application  
- `dao/JobApplicationDAO.py` – Contains all CRUD operations and SQL logic  
- `exception/exception_utils.py` – Custom reusable exception handling functions  
- `util/DBUtil.py` – Database connection utility using `pyodbc`

---

## 📌 Project Features

- ✅ Add, update, delete, and view job applications  
- ✅ Validates email format and application deadlines  
- ✅ Salary range validation and constraints  
- ✅ Graceful error handling with custom exceptions  
- ✅ Reusable and modular components following clean architecture principles  

---

## 🧱 Technologies Used

- **Language:** Python 3.x  
- **Database:** Microsoft SQL Server  
- **Library:** `pyodbc`  
- **Architecture:** DAO pattern + Utility & Exception modules  

---

## 🔍 Module Overviews

### `DBUtil.py`
- Establishes and manages SQL Server connection
- Reusable across DAO classes

### `JobApplicationDAO.py`
- Performs all database CRUD operations
- Handles query execution and result parsing

### `exception_utils.py`
- Contains reusable exception logic for:
  - Email validation
  - Salary boundary checks
  - Deadline validation
  - DB connection errors
  - File-related exceptions

### `main.py`
- CLI interface for end-users
- Accepts user input and routes commands to DAO methods
- Displays appropriate success or error messages

---

## 💡 Sample CLI Menu

```bash
Welcome to CareerHub!

1. Add Job Application
2. View All Applications
3. Update Application
4. Delete Application
5. Exit
Enter your choice:
```

---

## 🎯 Skills Demonstrated

- Object-Oriented Programming (OOP)
- Exception handling and validation
- CRUD operations via `pyodbc`
- Modular and scalable code structure
- Real-world CLI simulation

---

## 🔗 Links

- 🌐 [Portfolio Website](https://srishankar.netlify.app/)  
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/srishankar-lokanath/)  
- 📫 Email: [srishankarloknath@gmail.com](mailto:srishankarloknath@gmail.com)

---

## ⭐️ Like the Project?

If you found this helpful or inspiring, please **star** ⭐ the repository or **fork** 🍴 it to support and share. Your feedback is always welcome!
