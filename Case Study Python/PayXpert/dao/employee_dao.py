from interface.i_employee_service import IEmployeeService
from util.db_conn_util import DBConnUtil
from entity.employee import Employee
import pyodbc


class EmployeeDAO(IEmployeeService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_employee_by_id(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", employee_id)
            row = cursor.fetchone()
            if row:
                return Employee(*row)
            else:
                print(f"No employee found with ID {employee_id}.")
                return None
        except pyodbc.Error as e:
            print(f"Error occurred while fetching employee by ID: {e}")
            return None

    def get_all_employees(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Employee")
            employees = [Employee(*row) for row in cursor.fetchall()]
            if employees:
                return employees
            else:
                print("No employees found in the database.")
                return []
        except pyodbc.Error as e:
            print(f"Error occurred while fetching all employees: {e}")
            return []

    def add_employee(self, employee_data):
        try:
            cursor = self.conn.cursor()

            # Convert date fields to string format or None
            def format_date(val):
                if val is None:
                    return None
                return str(val) if isinstance(val, str) else val.strftime('%Y-%m-%d')

            cursor.execute("""
                INSERT INTO Employee (
                    FirstName, LastName, DateOfBirth, Gender, Email, 
                    PhoneNumber, Address, Position, JoiningDate, TerminationDate
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                employee_data.get_first_name(),
                employee_data.get_last_name(),
                format_date(employee_data.get_date_of_birth()),
                employee_data.get_gender(),
                employee_data.get_email(),
                employee_data.get_phone_number(),
                employee_data.get_address(),
                employee_data.get_position(),
                format_date(employee_data.get_joining_date()),
                format_date(employee_data.get_termination_date())
            ))

            self.conn.commit()

            print(f"Employee added successfully.")
        except pyodbc.Error as e:
            print(f"Error occurred while adding employee: {e}")

    def update_employee(self, employee_data):
        try:
            cursor = self.conn.cursor()

            # Convert datetime fields to strings or None
            def format_date(date_val):
                if date_val is None:
                    return None
                return str(date_val) if isinstance(date_val, str) else date_val.strftime('%Y-%m-%d')

            cursor.execute("""
                UPDATE Employee SET FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?,
                    PhoneNumber=?, Address=?, Position=?, JoiningDate=?, TerminationDate=?
                WHERE EmployeeID=?
            """, (
                employee_data.get_first_name(),
                employee_data.get_last_name(),
                format_date(employee_data.get_date_of_birth()),
                employee_data.get_gender(),
                employee_data.get_email(),
                employee_data.get_phone_number(),
                employee_data.get_address(),
                employee_data.get_position(),
                format_date(employee_data.get_joining_date()),
                format_date(employee_data.get_termination_date()),
                employee_data.get_employee_id()
            ))

            # Commit the changes
            self.conn.commit()

            # Check if any row was affected
            if cursor.rowcount > 0:
                print(f"Employee with ID {employee_data.get_employee_id()} was successfully updated.")
            else:
                print(f"No changes made for Employee ID {employee_data.get_employee_id()}. Perhaps the data is the same.")
        except pyodbc.Error as e:
            print(f"Error occurred while updating employee: {e}")

    def remove_employee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", employee_id)
            self.conn.commit()

            if cursor.rowcount > 0:
                print(f"Employee with ID {employee_id} removed successfully.")
            else:
                print(f"No employee found with ID {employee_id} to remove.")
        except pyodbc.Error as e:
            print(f"Error occurred while removing employee: {e}")
