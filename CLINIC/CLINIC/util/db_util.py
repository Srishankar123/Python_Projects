import pyodbc

class DBConnection:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LAPTOP-A3LRA9TF;'
            'DATABASE=appdb;' 
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()  # ✅ Define the cursor

    def get_cursor(self):
        return self.cursor  # ✅ Return the cursor object

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
