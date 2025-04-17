from datetime import date, datetime


class Employee:
    def __init__(self, employee_id=None, first_name="", last_name="", date_of_birth=None,
                 gender="", email="", phone_number="", address="", position="",
                 joining_date=None, termination_date=None):

        # Check if date_of_birth is provided as a string and convert it to a date object
        if isinstance(date_of_birth, str):
            self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date() if date_of_birth else None
        else:
            self.__date_of_birth = date_of_birth

        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__position = position
        self.__joining_date = joining_date
        self.__termination_date = termination_date
        self.gross_salary = 0  # Will be calculated
        self.net_salary = 0  # Will be calculated
        self.tax = 0  # Will be calculated

    # Getters and Setters
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, val):
        self.__employee_id = val

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, val):
        self.__first_name = val

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, val):
        self.__last_name = val

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, val):
        self.__date_of_birth = val

    def get_gender(self):
        return self.__gender

    def set_gender(self, val):
        self.__gender = val

    def get_email(self):
        return self.__email

    def set_email(self, val):
        self.__email = val

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, val):
        self.__phone_number = val

    def get_address(self):
        return self.__address

    def set_address(self, val):
        self.__address = val

    def get_position(self):
        return self.__position

    def set_position(self, val):
        self.__position = val

    def get_joining_date(self):
        return self.__joining_date

    def set_joining_date(self, val):
        self.__joining_date = val

    def get_termination_date(self):
        return self.__termination_date

    def set_termination_date(self, val):
        self.__termination_date = val




    # Method to calculate employee age
    def calculate_age(self):
        if self.__date_of_birth:
            today = date.today()
            return today.year - self.__date_of_birth.year - (
                    (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day)
            )
        return None

    # Method to provide a string representation of the object
    def __str__(self):
        return f"Employee ID: {self.__employee_id}, Name: {self.__first_name} {self.__last_name}, Position: {self.__position}, Email: {self.__email}, Age: {self.calculate_age()}"
