from datetime import datetime

class JobApplication:
    def __init__(self, application_id: int, job_id: int, applicant_id: int,
                 application_date: datetime, cover_letter: str):
        self._application_id = application_id
        self._job_id = job_id
        self._applicant_id = applicant_id
        self._application_date = application_date
        self._cover_letter = cover_letter

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Application ID must be an integer.")
        self._application_id = value

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Job ID must be an integer.")
        self._job_id = value

    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Applicant ID must be an integer.")
        self._applicant_id = value

    @property
    def application_date(self):
        return self._application_date

    @application_date.setter
    def application_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Application date must be a datetime object.")
        self._application_date = value

    @property
    def cover_letter(self):
        return self._cover_letter

    @cover_letter.setter
    def cover_letter(self, value):
        if not value or not value.strip():
            raise ValueError("Cover letter cannot be empty.")
        self._cover_letter = value.strip()
