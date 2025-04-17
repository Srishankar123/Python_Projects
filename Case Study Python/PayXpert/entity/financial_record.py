class FinancialRecord:
    def __init__(self, record_id=None, employee_id=None, record_date=None, description="", amount=0.0, record_type=""):
        self.__record_id = record_id
        self.__employee_id = employee_id
        self.__record_date = record_date
        self.__description = description
        self.__amount = amount
        self.__record_type = record_type

    # Getters and Setters
    def get_record_id(self): return self.__record_id
    def set_record_id(self, val): self.__record_id = val

    def get_employee_id(self): return self.__employee_id
    def set_employee_id(self, val): self.__employee_id = val

    def get_record_date(self): return self.__record_date
    def set_record_date(self, val): self.__record_date = val

    def get_description(self): return self.__description
    def set_description(self, val): self.__description = val

    def get_amount(self): return self.__amount
    def set_amount(self, val): self.__amount = val

    def get_record_type(self): return self.__record_type
    def set_record_type(self, val): self.__record_type = val

    # Method to provide a string representation of the object
    def __str__(self):
        return f"Record ID: {self.__record_id}, Employee ID: {self.__employee_id}, Date: {self.__record_date}, Description: {self.__description}, Amount: {self.__amount}, Type: {self.__record_type}"

