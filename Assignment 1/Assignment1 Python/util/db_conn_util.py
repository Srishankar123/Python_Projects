import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=LAPTOP-86110DUR;'
                'DATABASE=TechShop;'
                'Trusted_Connection=yes;'
            )
            return connection
        except Exception as e:
            print("Error connecting to database:", e)
            raise
