from datetime import datetime

class JobListing:
    def __init__(self, company_id, job_title, job_description, job_location,
                 salary, job_type, posted_date, job_id=None):
        self._job_id = job_id
        self._company_id = company_id
        self._job_title = job_title
        self._job_description = job_description
        self._job_location = job_location
        self._salary = salary
        self._job_type = job_type
        self._posted_date = posted_date

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Company ID must be an integer.")
        self._company_id = value

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        if not value or not value.strip():
            raise ValueError("Job title cannot be empty.")
        self._job_title = value.strip()

    @property
    def job_description(self):
        return self._job_description

    @job_description.setter
    def job_description(self, value):
        if not value or not value.strip():
            raise ValueError("Job description cannot be empty.")
        self._job_description = value.strip()

    @property
    def job_location(self):
        return self._job_location

    @job_location.setter
    def job_location(self, value):
        if not value or not value.strip():
            raise ValueError("Job location cannot be empty.")
        self._job_location = value.strip()

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Salary must be a non-negative number.")
        self._salary = value

    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        if not value or not value.strip():
            raise ValueError("Job type cannot be empty.")
        self._job_type = value.strip()

    @property
    def posted_date(self):
        return self._posted_date

    @posted_date.setter
    def posted_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Posted date must be a datetime object.")
        self._posted_date = value
