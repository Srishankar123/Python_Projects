import re
import os
from datetime import datetime
import pyodbc

# ---------- 1. Email Validation ----------
def register_applicant_email():
    email = input("Enter your email address: ").strip()
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format.")
    return email

def is_valid_email(email: str) -> bool:
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# ---------- 2. Salary Calculation ----------
def calculate_average_salary(job_salaries):
    valid_salaries = [s for s in job_salaries.values() if s >= 0]
    if not valid_salaries:
        raise ValueError("No valid salaries to calculate average.")
    return sum(valid_salaries) / len(valid_salaries)

# ---------- 3. File Upload ----------
def upload_resume(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found.")

    allowed_extensions = ['.pdf', '.doc', '.docx']
    file_size = os.path.getsize(file_path)

    if file_size > 5 * 1024 * 1024:
        raise Exception("File size exceeds 5MB limit.")

    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        raise Exception("Unsupported file format.")

# ---------- 4. Application Deadline ----------
def check_application_deadline(submission_date_str, deadline_str):
    submission_date = datetime.strptime(submission_date_str, "%Y-%m-%d")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    if submission_date > deadline:
        raise Exception("The application deadline has passed.")

# ---------- 5. DB Test (for demo/testing purposes only) ----------
def fetch_job_listings():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=LAPTOP-86110DUR;"
            "DATABASE=CareerHub;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT JobID, JobTitle FROM Jobs")
        jobs = cursor.fetchall()

        print("✅ Job Listings Retrieved:")
        for job in jobs:
            print(f"  - {job.JobID}: {job.JobTitle}")

    except pyodbc.Error as db_err:
        print(f"❌ Database Error: {db_err}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")



# -------------------- Demo Calls --------------------
'''
if __name__ == "__main__":
    print("------ Email Validation ------")
    register_applicant_email()

    print("\n------ Salary Calculation ------")
    job_salaries = {
        101: 55000,
        102: 65000,
        103: -10000  # This will trigger an exception
    }
    calculate_average_salary(job_salaries)

    print("\n------ Resume Upload ------")
    upload_resume("lol.pdf")  # Change this to a real file for testing

    print("\n------ Application Deadline Check ------")
    check_application_deadline("2025-04-09", "2025-04-01")

    print("\n------ Database Connection ------")
    fetch_job_listings()
'''