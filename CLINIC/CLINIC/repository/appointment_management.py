from model.patient import Patient
from exception.patient_not_found_exception import PatientNotFoundException
from util.db_util import DBConnection

class AppointmentManagement:
    def __init__(self):
        self.db = DBConnection()
        self.cursor = self.db.get_cursor()

    def add_patient(self,name,age,gender,symptoms,contact):
        try:
            self.cursor.execute(
                "insert into Patients (name, age, gender, symptoms, contact) values (?,?,?,?,?)",
                (name,age,gender,symptoms, contact)
            )
            self.db.commit()
            return True
        except:
            return False
        
    def update_patient_contact(self, patient_id, contact):
        try:
            self.cursor.execute("UPDATE Patients SET contact = ? WHERE patient_id = ?", (contact, patient_id))
            if self.cursor.rowcount == 0:
                raise PatientNotFoundException()
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error while updating patient contact: {e}")
            return False

    def delete_patient(self, patient_id):
        try:
            self.cursor.execute("DELETE FROM Patients WHERE patient_id = ?", (patient_id,))
            if self.cursor.rowcount == 0:
                raise PatientNotFoundException()
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error while deleting patient: {e}")
            return False

    def get_all_patients(self):
        try:
            self.cursor.execute("SELECT * FROM Patients")
            rows = self.cursor.fetchall()
            return [Patient(*row) for row in rows]
        except Exception as e:
            print(f"Error while fetching all patients: {e}")
            return []

    def search_patient(self, search_term):
        try:
            self.cursor.execute("SELECT * FROM Patients WHERE name LIKE ? OR symptoms LIKE ?", 
                                (f"%{search_term}%", f"%{search_term}%"))
            rows = self.cursor.fetchall()
            if not rows:
                raise PatientNotFoundException()
            return [Patient(*row) for row in rows]
        except Exception as e:
            print(f"Error while searching for patient: {e}")
            return []

    def filter_by_age(self, threshold):
        try:
            self.cursor.execute("SELECT * FROM Patients WHERE age > ?", (threshold,))
            rows = self.cursor.fetchall()
            return [Patient(*row) for row in rows]
        except Exception as e:
            print(f"Error while filtering patients by age: {e}")
            return []

    def close_connection(self):
        self.db.close()
