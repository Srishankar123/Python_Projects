import pyodbc
from util.db_conn_util import DBConnUtil
from entity.job_listing import JobListing
from entity.company import Company
from entity.applicant import Applicant
from entity.job_application import JobApplication

class DatabaseManager:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def initialize_database(self):
        cursor = self.conn.cursor()

        # Create Companies table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Companies (
            CompanyID INT PRIMARY KEY IDENTITY,
            CompanyName VARCHAR(255),
            Location VARCHAR(255)
        )
        """)

        # Create JobListings table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Jobs (
            JobID INT PRIMARY KEY IDENTITY,
            CompanyID INT,
            JobTitle VARCHAR(255),
            JobDescription TEXT,
            JobLocation VARCHAR(255),
            Salary DECIMAL(18, 2),
            JobType VARCHAR(50),
            PostedDate DATETIME,
            FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
        )
        """)

        # Create Applicants table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Applicants (
            ApplicantID INT PRIMARY KEY IDENTITY,
            FirstName VARCHAR(100),
            LastName VARCHAR(100),
            Email VARCHAR(255),
            Phone VARCHAR(20),
            Resume TEXT
        )
        """)

        # Create JobApplications table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Applications (
            ApplicationID INT PRIMARY KEY IDENTITY,
            JobID INT,
            ApplicantID INT,
            ApplicationDate DATETIME,
            CoverLetter TEXT,
            FOREIGN KEY (JobID) REFERENCES JobListings(JobID),
            FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
        )
        """)

        self.conn.commit()
        print("✅ Database initialized.")

    def insert_job_listing(self, job: JobListing):
        cursor = self.conn.cursor()
        query = """
        INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            job.company_id,
            job.job_title,
            job.job_description,
            job.job_location,
            job.salary,
            job.job_type,
            job.posted_date
        ))
        self.conn.commit()

    def insert_company(self, company: Company):
        cursor = self.conn.cursor()
        query = "INSERT INTO Companies (CompanyName, Location) VALUES (?, ?)"
        cursor.execute(query, (company.company_name, company.location))
        self.conn.commit()

    def insert_applicant(self, applicant: Applicant):
        cursor = self.conn.cursor()
        query = """
        INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            applicant.first_name,
            applicant.last_name,
            applicant.email,
            applicant.phone,
            applicant.resume
        ))
        self.conn.commit()

    def insert_job_application(self, application: JobApplication):
        cursor = self.conn.cursor()
        query = """
        INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (
            application.job_id,
            application.applicant_id,
            application.application_date,
            application.cover_letter
        ))
        self.conn.commit()

    def get_job_listings(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Jobs")
        return cursor.fetchall()

    def get_companies(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Companies")
        return cursor.fetchall()

    def get_applicants(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Applicants")
        return cursor.fetchall()

    def get_applications_for_job(self, job_id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Applications WHERE JobID = ?", (job_id,))
        return cursor.fetchall()
