from repository.appointment_management import AppointmentManagement
from exception.patient_not_found_exception import PatientNotFoundException
from util.db_util import DBConnection  # ✅ Import DBConnection

def main():
    try:
        db = DBConnection()
        print("Database connection successful!")

        am = AppointmentManagement()

        while True:
            print("\nClinic Appointment Management")
            print("1. Add patient\n2. Update contact\n3. Delete patient\n4. View all patients\n5. Search patients\n6. Filter by age\n7. Exit")
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    name = input("Name: ")
                    age = int(input("Age: "))
                    gender = input("Gender: ")
                    symptoms = input("Symptoms: ")
                    contact = input("Contact: ")
                    if am.add_patient(name, age, gender, symptoms, contact):
                        print("Patient added successfully.")
                    else:
                        print("Error adding patient.")
                elif choice == 2:
                    pid = int(input("Enter Patient ID: "))
                    contact = input("Enter new contact: ")
                    try:
                        if am.update_patient_contact(pid, contact):
                            print("Contact updated.")
                    except PatientNotFoundException as e:
                        print(e)
                elif choice == 3:
                    pid = int(input("Enter Patient ID to delete: "))
                    try:
                        if am.delete_patient(pid):
                            print("Patient deleted.")
                    except PatientNotFoundException as e:
                        print(e)
                elif choice == 4:
                    patients = am.get_all_patients()
                    for p in patients:
                        print("\n" + str(p))
                elif choice == 5:
                    term = input("Enter name or symptom to search: ")
                    try:
                        results = am.search_patient(term)
                        for p in results:
                            print("\n" + str(p))
                    except PatientNotFoundException as e:
                        print(e)
                elif choice == 6:
                    age = int(input("Enter age threshold: "))
                    filtered = am.filter_by_age(age)
                    for p in filtered:
                        print("\n" + str(p))
                elif choice == 7:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice")
            except Exception as e:
                print("Error:", e)

        am.close_connection()
        db.close()

    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    main()
