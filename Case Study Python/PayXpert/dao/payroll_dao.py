from interface.i_payroll_service import IPayrollService
from entity.payroll import Payroll
import pyodbc
from util.db_conn_util import DBConnUtil


class PayrollDAO(IPayrollService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def generate_payroll(self, employee_id, start_date, end_date):
        try:
            cursor = self.conn.cursor()

            # Sample calculation logic (you can update this to your business logic)
            cursor.execute("SELECT BasicSalary FROM Payroll WHERE EmployeeID = ?", employee_id)
            row = cursor.fetchone()
            if not row:
                print("Employee not found")
                return

            basic_salary = row[0]
            overtime_pay = 500  # Dummy value
            deductions = 200    # Dummy value
            net_salary = basic_salary + overtime_pay - deductions #Which is
            # already defined in my sql database so it is not used here

            cursor.execute("""
                INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions)
                    VALUES (?, ?, ?, ?, ?, ?)
            """, (
                employee_id,
                start_date,
                end_date,
                basic_salary,
                overtime_pay,
                deductions
            ))
            self.conn.commit()
            print("Payroll generated.")
        except pyodbc.Error as e:
            print("Error generating payroll:", e)

    def get_payroll_by_id(self, payroll_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", payroll_id)
            row = cursor.fetchone()
            return Payroll(*row) if row else None
        except pyodbc.Error as e:
            print("Error fetching payroll by ID:", e)

    def get_payrolls_for_employee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", employee_id)
            return [Payroll(*row) for row in cursor.fetchall()]
        except pyodbc.Error as e:
            print("Error fetching payrolls for employee:", e)
            return []

    def get_payrolls_for_period(self, start_date, end_date):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """, (start_date, end_date))
            return [Payroll(*row) for row in cursor.fetchall()]
        except pyodbc.Error as e:
            print("Error fetching payrolls for period:", e)
            return []

