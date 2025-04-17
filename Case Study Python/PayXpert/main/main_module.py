from dao.employee_dao import EmployeeDAO
from dao.payroll_dao import PayrollDAO
from dao.tax_dao import TaxDAO
from dao.financial_record_dao import FinancialRecordDAO
from entity.employee import Employee
from exception.user_exceptions import (
    EmployeeNotFoundException,
    PayrollGenerationException,
    TaxCalculationException,
    FinancialRecordException,
    InvalidInputException,
    DatabaseConnectionException
)
from datetime import datetime
import uuid

employee_dao = EmployeeDAO()
payroll_dao = PayrollDAO()
tax_dao = TaxDAO()
financial_dao = FinancialRecordDAO()

def employee_service_dashboard():
    while True:
        print("\n=== Employee Service Dashboard ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. Back to Admin Dashboard")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                position = input("Position: ")
                joining_date = input("Joining Date (YYYY-MM-DD): ")
                termination_date = input("Termination Date (YYYY-MM-DD) or leave blank: ") or None

                employee_id = str(uuid.uuid4())[:8]  # Or however you prefer to generate it
                employee_data = Employee(
                    employee_id, first_name, last_name, dob, gender, email, phone,
                    address, position, joining_date, termination_date
                )
                employee_dao.add_employee(employee_data)
            except (InvalidInputException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '2':
            try:
                employees = employee_dao.get_all_employees()
                for emp in employees:
                    print(emp)
            except DatabaseConnectionException as e:
                print(e)


        elif choice == '3':
            try:
                emp_id = int(input("Employee ID to update: "))
                employee = employee_dao.get_employee_by_id(emp_id)
                print("Leave blank to keep current value.")
                employee.set_first_name(input(f"First Name ({employee.get_first_name()}): ") or employee.get_first_name())
                employee.set_last_name(input(f"Last Name ({employee.get_last_name()}): ") or employee.get_last_name())
                employee.set_date_of_birth(input(f"Date of Birth ({employee.get_date_of_birth()}): ") or employee.get_date_of_birth())
                employee.set_gender(input(f"Gender ({employee.get_gender()}): ") or employee.get_gender())
                employee.set_email(input(f"Email ({employee.get_email()}): ") or employee.get_email())
                employee.set_phone_number(input(f"Phone ({employee.get_phone_number()}): ") or employee.get_phone_number())
                employee.set_address(input(f"Address ({employee.get_address()}): ") or employee.get_address())
                employee.set_position(input(f"Position ({employee.get_position()}): ") or employee.get_position())
                employee.set_joining_date(input(f"Joining Date ({employee.get_joining_date()}): ") or employee.get_joining_date())
                termination_input = input(f"Termination Date ({employee.get_termination_date()}): ")
                employee.set_termination_date(termination_input if termination_input.strip() else None)
                employee_dao.update_employee(employee)
            except EmployeeNotFoundException as e:
                print(e)
            except (InvalidInputException, DatabaseConnectionException) as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter numeric values where required.")

        elif choice == '4':
            try:
                emp_id = int(input("Employee ID to remove: "))
                employee_dao.remove_employee(emp_id)
                print("Employee removed.")
            except EmployeeNotFoundException as e:
                print(e)
            except DatabaseConnectionException as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a valid employee ID.")

        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def payroll_service_dashboard():
    while True:
        print("\n=== Payroll Service Dashboard ===")
        print("1. Generate Payroll")
        print("2. View Payrolls for Employee")
        print("3. Get Payroll by ID")
        print("4. Get Payrolls for Period")
        print("5. Back to Admin Dashboard")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                payroll_dao.generate_payroll(emp_id, start_date, end_date)
            except (PayrollGenerationException, EmployeeNotFoundException, InvalidInputException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '2':
            try:
                emp_id = int(input("Enter Employee ID: "))
                records = payroll_dao.get_payrolls_for_employee(emp_id)
                for rec in records:
                    print(rec)
            except (EmployeeNotFoundException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '3':
            try:
                payroll_id = int(input("Enter Payroll ID: "))
                record = payroll_dao.get_payroll_by_id(payroll_id)
                if record:
                    print(record)
                else:
                    print("Payroll not found.")
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '4':
            try:
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                records = payroll_dao.get_payrolls_for_period(start_date, end_date)
                for rec in records:
                    print(rec)
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def tax_service_dashboard():
    while True:
        print("\n=== Tax Service Dashboard ===")
        print("1. Calculate Tax for Employee")
        print("2. View Tax by ID")
        print("3. View Taxes by Employee")
        print("4. View Taxes by Year")
        print("5. Back to Admin Dashboard")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                tax_year = int(input("Enter Tax Year: "))
                tax_dao.calculate_tax(emp_id, tax_year)
            except (TaxCalculationException, EmployeeNotFoundException, InvalidInputException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '2':
            try:
                tax_id = int(input("Enter Tax ID: "))
                tax = tax_dao.get_tax_by_id(tax_id)
                if tax:
                    print(tax)
                else:
                    print("Tax record not found.")
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '3':
            try:
                emp_id = int(input("Enter Employee ID: "))
                taxes = tax_dao.get_taxes_for_employee(emp_id)
                for t in taxes:
                    print(t)
            except (EmployeeNotFoundException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '4':
            try:
                year = int(input("Enter Tax Year: "))
                taxes = tax_dao.get_taxes_for_year(year)
                for t in taxes:
                    print(t)
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def financial_record_service_dashboard():
    while True:
        print("\n=== Financial Record Service Dashboard ===")
        print("1. Add Financial Record")
        print("2. View Financial Records by Employee")
        print("3. View Financial Record by ID")
        print("4. View Financial Records by Date")
        print("5. Back to Admin Dashboard")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                desc = input("Description: ")
                amount = float(input("Amount: "))
                record_type = input("Record Type (Income/Expense): ").strip()

                if record_type not in ['Income', 'Expense']:
                    raise InvalidInputException("Invalid record type. Must be 'Income' or 'Expense'.")

                financial_dao.add_financial_record(emp_id, desc, amount, record_type)
            except (FinancialRecordException, EmployeeNotFoundException, InvalidInputException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '2':
            try:
                emp_id = int(input("Enter Employee ID: "))
                records = financial_dao.get_financial_records_for_employee(emp_id)
                if records:
                    for r in records:
                        print(r)
                else:
                    print("No records found for this employee.")
            except (EmployeeNotFoundException, DatabaseConnectionException) as e:
                print(e)

        elif choice == '3':
            try:
                record_id = int(input("Enter Financial Record ID: "))
                record = financial_dao.get_financial_record_by_id(record_id)
                if record:
                    print(record)
                else:
                    print("Record not found.")
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '4':
            try:
                record_date = input("Enter Record Date (YYYY-MM-DD): ")
                records = financial_dao.get_financial_records_for_date(record_date)
                if records:
                    for r in records:
                        print(r)
                else:
                    print("No records found for this date.")
            except DatabaseConnectionException as e:
                print(e)

        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\n=== Admin Dashboard ===")
        print("1. Employee Service")
        print("2. Payroll Service")
        print("3. Tax Service")
        print("4. Financial Record Service")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            employee_service_dashboard()
        elif choice == '2':
            payroll_service_dashboard()
        elif choice == '3':
            tax_service_dashboard()
        elif choice == '4':
            financial_record_service_dashboard()
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    print("=== Welcome to PayXpert ===")
    print("1. Admin")
    role = input("Enter your role (1 for Admin): ")
    if role == '1':
        admin_menu()
    else:
        print("Invalid role. Exiting.")