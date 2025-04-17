class Applicant:
    def __init__(self, applicant_id: int, first_name: str, last_name: str,
                 email: str, phone: str, resume: str):
        self._applicant_id = applicant_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._resume = resume

    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Applicant ID must be an integer.")
        self._applicant_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value:
            raise ValueError("Invalid email address.")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit() or len(value) not in [10, 11, 12]:
            raise ValueError("Phone number must be digits and 10-12 characters long.")
        self._phone = value

    @property
    def resume(self):
        return self._resume

    @resume.setter
    def resume(self, value):
        if not value:
            raise ValueError("Resume path cannot be empty.")
        self._resume = value
