class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None,
                 taxable_income=0.0, tax_amount=0.0):
        self.__tax_id = tax_id
        self.__employee_id = employee_id
        self.__tax_year = tax_year
        self.__taxable_income = taxable_income
        self.__tax_amount = tax_amount

    # Getters and setters

    def get_tax_id(self):
        return self.__tax_id

    def set_tax_id(self, tax_id):
        self.__tax_id = tax_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_tax_year(self):
        return self.__tax_year

    def set_tax_year(self, tax_year):
        self.__tax_year = tax_year

    def get_taxable_income(self):
        return self.__taxable_income

    def set_taxable_income(self, taxable_income):
        self.__taxable_income = taxable_income

    def get_tax_amount(self):
        return self.__tax_amount

    def set_tax_amount(self, tax_amount):
        self.__tax_amount = tax_amount


    def __str__(self):
        return (
            f"Tax ID: {self.__tax_id}, Employee ID: {self.__employee_id}, Year: {self.__tax_year}\n"
            f"Taxable Income: ${self.__taxable_income:,.2f}, Tax Amount: ${self.__tax_amount:,.2f}"
        )
