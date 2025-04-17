from interface.i_financial_record_service import IFinancialRecordService
from entity.financial_record import FinancialRecord
import pyodbc
from util.db_conn_util import DBConnUtil


class FinancialRecordDAO(IFinancialRecordService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def add_financial_record(self, employee_id, description, amount, record_type):
        try:
            # Strip extra spaces
            record_type = record_type.strip()

            # Validate that the record type is either 'Income' or 'Expense'
            if record_type not in ['Income', 'Expense']:
                raise ValueError("Record type must be either 'Income' or 'Expense'.")

            # Proceed to insert into the database
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
                VALUES (?, GETDATE(), ?, ?, ?)
            """, (employee_id, description, amount, record_type))
            self.conn.commit()
            print("Financial record added successfully.")
        except (ValueError, pyodbc.Error) as e:
            print("Error adding financial record:", e)

    def get_financial_record_by_id(self, record_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = ?", record_id)
            row = cursor.fetchone()
            return FinancialRecord(*row) if row else None
        except pyodbc.Error as e:
            print("Error fetching record by ID:", e)

    def get_financial_records_for_employee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = ?", employee_id)
            rows = cursor.fetchall()
            return [FinancialRecord(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error fetching records for employee:", e)
            return []

    def get_financial_records_for_date(self, record_date):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE CAST(RecordDate AS DATE) = ?", record_date)
            rows = cursor.fetchall()
            return [FinancialRecord(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error fetching records for date:", e)
            return []
