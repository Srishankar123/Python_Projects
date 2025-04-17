import pyodbc
from datetime import datetime
from entity.job_application import JobApplication
from entity.applicant import Applicant
from util.db_conn_util import DBConnUtil

class JobApplicationDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def apply(self, job_id: int, applicant_id: int, cover_letter: str):
        cursor = self.conn.cursor()
        application_date = datetime.now()

        insert_query = """
        INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (job_id, applicant_id, application_date, cover_letter))
        self.conn.commit()
        print(f"✅ Applicant {applicant_id} successfully applied for Job {job_id}.")

    def get_applicants(self, job_id: int):
        cursor = self.conn.cursor()
        query = """
        SELECT A.ApplicantID, A.FirstName, A.LastName, A.Email, A.Phone, A.Resume
        FROM Applications JA
        JOIN Applicants A ON JA.ApplicantID = A.ApplicantID
        WHERE JA.JobID = ?
        """
        cursor.execute(query, (job_id,))
        rows = cursor.fetchall()

        applicants = []
        for row in rows:
            applicants.append(Applicant(*row))
        return applicants
