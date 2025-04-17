import pyodbc
from datetime import datetime
from entity.applicant import Applicant
from exception.user_defined_exception import check_application_deadline
from util.db_conn_util import DBConnUtil
from exception.user_defined_exception import upload_resume, check_application_deadline


class ApplicantDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def create_profile(self, email: str, first_name: str, last_name: str, phone: str, resume: str = ""):
        cursor = self.conn.cursor()

        insert_query = """
        INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (first_name, last_name, email, phone, resume))
        self.conn.commit()

        print(f"✅ Profile created for {first_name} {last_name}.")


    def fetch_job_listings(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT j.JobTitle, c.CompanyName, j.Salary FROM Jobs j JOIN Companies c ON j.CompanyID = c.CompanyID")
            jobs = cursor.fetchall()

            print("\n✅ Job Listings:")
            for job in jobs:
                print(f"  - {job.JobTitle} at {job.CompanyName}: ₹{job.Salary}")
        except pyodbc.Error as db_err:
            print(f"❌ Database Error: {db_err}")

    def create_applicant_profile(self, email, first_name, last_name, phone, resume):
        try:
            upload_resume(resume)  # Validate the resume upload

            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?)""",
                           (first_name, last_name, email, phone, resume))
            self.conn.commit()
            print("✅ Applicant profile created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def apply_for_job(self, applicant_id, job_id, cover_letter):
        try:
            submission_date = datetime.now().strftime("%Y-%m-%d")
            check_application_deadline(submission_date, "2025-12-31")

            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?)""",
                           (job_id, applicant_id, submission_date, cover_letter))
            self.conn.commit()
            print("✅ Application submitted successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def salary_range_query(self, min_salary, max_salary):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT j.JobTitle, c.CompanyName, j.Salary
                FROM Jobs j
                JOIN Companies c ON j.CompanyID = c.CompanyID
                WHERE j.Salary BETWEEN ? AND ?""",
                           (min_salary, max_salary))
            results = cursor.fetchall()

            print("✅ Jobs within salary range:")
            for job in results:
                print(f"  - {job.JobTitle} at {job.CompanyName}: ₹{job.Salary}")
        except Exception as e:
            print(f"❌ Error: {e}")
