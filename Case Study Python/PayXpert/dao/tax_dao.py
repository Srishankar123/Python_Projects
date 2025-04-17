from decimal import Decimal
import pyodbc
from util.db_conn_util import DBConnUtil
from interface.i_tax_service import ITaxService
from entity.tax import Tax

class TaxDAO(ITaxService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def calculate_tax(self, employee_id, tax_year):
        try:
            cursor = self.conn.cursor()

            # Dummy logic: Get payrolls and sum taxable income
            cursor.execute("""
                SELECT SUM(NetSalary) FROM Payroll
                WHERE EmployeeID = ? AND YEAR(PayPeriodEndDate) = ?
            """, (employee_id, tax_year))

            row = cursor.fetchone()
            taxable_income = row[0] if row[0] else Decimal(0)  # Ensure taxable_income is Decimal

            # Convert the tax rate to Decimal to avoid type mismatch
            tax_rate = Decimal("0.1")  # Convert tax rate to Decimal

            # Calculate the tax amount (ensure Decimal with proper precision)
            tax_amount = (taxable_income * tax_rate).quantize(Decimal("0.01"))  # Rounded to 2 decimal places

            # Insert the tax record into the Tax table
            cursor.execute("""
                INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
                VALUES (?, ?, ?, ?)
            """, (employee_id, tax_year, taxable_income, tax_amount))

            self.conn.commit()
            print("Tax record generated.")
        except pyodbc.Error as e:
            print("Error calculating tax:", e)

    def get_tax_by_id(self, tax_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", tax_id)
            row = cursor.fetchone()
            return Tax(*row) if row else None
        except pyodbc.Error as e:
            print("Error fetching tax by ID:", e)

    def get_taxes_for_employee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", employee_id)
            return [Tax(*row) for row in cursor.fetchall()]
        except pyodbc.Error as e:
            print("Error fetching taxes for employee:", e)
            return []

    def get_taxes_for_year(self, tax_year):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", tax_year)
            return [Tax(*row) for row in cursor.fetchall()]
        except pyodbc.Error as e:
            print("Error fetching taxes for year:", e)
            return []
