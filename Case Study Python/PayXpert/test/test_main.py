import pytest
from pytest import approx
from decimal import Decimal

# Sample Employee class
class Employee:
    def __init__(self, basic_salary=0, allowance=0, bonus=0, gross_salary=0, tax_deduction=0, insurance_deduction=0):
        self.basic_salary = Decimal(basic_salary)
        self.allowance = Decimal(allowance)
        self.bonus = Decimal(bonus)
        self.gross_salary = Decimal(gross_salary)
        self.tax_deduction = Decimal(tax_deduction)
        self.insurance_deduction = Decimal(insurance_deduction)


# Sample PayrollService class
class PayrollService:
    def calculate_gross_salary(self, employee):
        return employee.basic_salary + employee.allowance + employee.bonus

    def calculate_net_salary(self, employee):
        if employee.gross_salary < 0:
            raise ValueError("Salary cannot be negative.")
        if employee.tax_deduction < 0:
            raise ValueError("Tax deduction cannot be negative.")
        return employee.gross_salary - (employee.tax_deduction + employee.insurance_deduction)

    def calculate_tax(self, employee):
        if employee.gross_salary < 0:
            raise ValueError("Salary cannot be negative.")
        if employee.tax_deduction < 0:
            raise ValueError("Tax deduction cannot be negative.")
        return employee.gross_salary * Decimal(0.2)

    def process_payroll(self, employees):
        processed_employees = []
        for employee in employees:
            processed_employees.append(employee)  # In reality, this would save to a database
        return processed_employees


# Test cases using pytest

@pytest.fixture
def employee():
    return Employee(basic_salary=5000, allowance=1000, bonus=500)

def test_calculate_gross_salary_for_employee(employee):
    payroll_service = PayrollService()
    gross_salary = payroll_service.calculate_gross_salary(employee)
    # Test Case: Calculate Gross Salary for Employee
    assert gross_salary == 6500, f"Expected 6500, but got {gross_salary}"

@pytest.fixture
def employee_with_deductions():
    return Employee(gross_salary=6500, tax_deduction=500, insurance_deduction=200)

def test_calculate_net_salary_after_deductions(employee_with_deductions):
    payroll_service = PayrollService()
    net_salary = payroll_service.calculate_net_salary(employee_with_deductions)
    # Test Case: Calculate Net Salary After Deductions
    assert net_salary == 5800, f"Expected 5800, but got {net_salary}"

@pytest.fixture
def high_income_employee():
    return Employee(gross_salary=20000)

def test_verify_tax_calculation_for_high_income_employee(high_income_employee):
    payroll_service = PayrollService()
    tax_amount = payroll_service.calculate_tax(high_income_employee)
    # Test Case: Verify Tax Calculation for High Income Employee
    assert tax_amount == 4000, f"Expected 4000, but got {tax_amount}"

@pytest.fixture
def multiple_employees():
    return [
        Employee(gross_salary=5000, tax_deduction=500, insurance_deduction=200),
        Employee(gross_salary=7000, tax_deduction=700, insurance_deduction=250),
        Employee(gross_salary=9000, tax_deduction=900, insurance_deduction=300)
    ]

def test_verify_tax_calculation_for_high_income_employee(high_income_employee):
    payroll_service = PayrollService()
    tax_amount = payroll_service.calculate_tax(high_income_employee)
    # Use pytest.approx() for floating-point comparison
    assert tax_amount == approx(4000, rel=1e-9), f"Expected 4000, but got {tax_amount}"


def test_invalid_salary_throws_exception():
    invalid_employee = Employee(gross_salary=-1000)
    payroll_service = PayrollService()
    # Test Case: Verify Error Handling for Invalid Employee Data (Invalid Salary)
    with pytest.raises(ValueError, match="Salary cannot be negative."):
        payroll_service.calculate_net_salary(invalid_employee)

def test_invalid_tax_deduction_throws_exception():
    invalid_employee = Employee(gross_salary=5000, tax_deduction=-500)
    payroll_service = PayrollService()
    # Test Case: Verify Error Handling for Invalid Employee Data (Invalid Tax Deduction)
    with pytest.raises(ValueError, match="Tax deduction cannot be negative."):
        payroll_service.calculate_tax(invalid_employee)
