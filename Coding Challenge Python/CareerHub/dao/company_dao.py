import pyodbc
from datetime import datetime
from entity.job_listing import JobListing
from util.db_conn_util import DBConnUtil

class CompanyDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def post_job(self, company_id: int, job_title: str, job_description: str,
                 job_location: str, salary: float, job_type: str):
        cursor = self.conn.cursor()
        posted_date = datetime.now()

        insert_query = """
        INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (company_id, job_title, job_description,
                                      job_location, salary, job_type, posted_date))
        self.conn.commit()
        print(f"✅ Job '{job_title}' posted by Company ID {company_id}.")

    def get_jobs(self, company_id: int):
        cursor = self.conn.cursor()
        query = """
        SELECT JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate
        FROM Jobs
        WHERE CompanyID = ?
        """
        cursor.execute(query, (company_id,))
        rows = cursor.fetchall()

        job_listings = []
        for row in rows:
            job_listings.append(JobListing(*row))
        return job_listings
