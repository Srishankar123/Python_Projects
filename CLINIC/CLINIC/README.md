# 🏥 Clinic Appointment Management System

A console-based application to manage patient appointments, built using **Python**, **pyodbc**, and **MS SQL Server**. This system streamlines common operations like patient registration, updating details, searching, and filtering, with secure database interaction.

## 📌 Features

- ✅ Register new patient appointments  
- 🔁 Update patient details  
- ❌ Delete patient records  
- 🔍 Search patients by name or contact  
- 🎯 Filter patients by appointment date or doctor  
- 🔐 Secure CRUD operations using **parameterized SQL queries**  
- 🧩 Modular structure with DAO (Data Access Object) and Exception Handling  

## 🛠️ Tech Stack

- **Backend:** Python  
- **Database:** Microsoft SQL Server  
- **Connector:** pyodbc  

## 📂 Project Structure

```
CLINIC/
├── exception/
│   └── PatientNotFoundException.py
├── model/
│   └── Patient.py
├── repository/
│   └── AppointmentManagement.py
├── util/
│   └── DBConnection.py
└── main.py
```

### Module Overview

- `model/Patient.py`: Defines the `Patient` class with attributes like name, age, gender, contact, doctor, and appointment date.  
- `repository/AppointmentManagement.py`: Contains logic for all database operations.  
- `util/DBConnection.py`: Manages database connectivity using pyodbc.  
- `exception/PatientNotFoundException.py`: Custom exception for handling missing patient cases.  
- `main.py`: CLI interface to perform operations.  

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Srishankar123/Python_Projects.git
cd Python_Projects/CLINIC/CLINIC
```

### 2. Setup your database
- Use Microsoft SQL Server.
- Create a table `Patient` with appropriate columns.
- Update your DB credentials in `util/DBConnection.py`.

### 3. Install dependencies
```bash
pip install pyodbc
```

### 4. Run the application
```bash
python main.py
```

## 📷 Screenshots

*(You can optionally include CLI output screenshots here)*

## 🧠 Concepts Applied

- Object-Oriented Programming (OOP)  
- Exception Handling  
- Database Connectivity with `pyodbc`  
- Modular Python Design (separation of concerns)  

## 📌 Author

**Srishankar Lokanath**  
📫 [srishankarloknath@gmail.com](mailto:srishankarloknath@gmail.com)  
🔗 [Portfolio](https://srishankar.netlify.app/) | [GitHub](https://github.com/Srishankar123) | [LinkedIn](https://linkedin.com/in/srishankar)

---

⭐ *If you found this project helpful, feel free to star the repository!*
