

class EmployeeNotFoundException(Exception):
    def __init__(self, message="Employee not found."):
        super().__init__(message)


class PayrollGenerationException(Exception):
    def __init__(self, message="Error generating payroll for the employee."):
        super().__init__(message)


class TaxCalculationException(Exception):
    def __init__(self, message="Error calculating tax for the employee."):
        super().__init__(message)


class FinancialRecordException(Exception):
    def __init__(self, message="Error with financial record management."):
        super().__init__(message)


class InvalidInputException(Exception):
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)


class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection error."):
        super().__init__(message)
