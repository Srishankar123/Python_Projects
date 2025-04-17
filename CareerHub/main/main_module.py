from datetime import datetime

from dao.applicant_dao import ApplicantDAO
from dao.database_manager import DatabaseManager
from entity.company import Company
from entity.job_listing import JobListing


def admin_menu():
    admin_dao = DatabaseManager()

    while True:
        print("\nAdmin Menu:")
        print("1. Initialize Database")
        print("2. Add Company")
        print("3. Post Job Listing")
        print("4. View All Companies")
        print("5. View All Job Listings")
        print("6. View All Applicants")
        print("7. View Applications for a Job")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_dao.initialize_database()
        elif choice == "2":
            name = input("Enter company name: ")
            location = input("Enter location: ")
            admin_dao.insert_company(Company(company_name=name, location=location))
        elif choice == "3":
            cid = int(input("Enter Company ID: "))
            title = input("Enter Job Title: ")
            desc = input("Enter Job Description: ")
            loc = input("Enter Job Location: ")
            salary = float(input("Enter Salary: "))
            jtype = input("Enter Job Type (Full-time/Part-time): ")
            date = datetime.now()
            admin_dao.insert_job_listing(JobListing(company_id=cid, job_title=title, job_description=desc,
                                                    job_location=loc, salary=salary, job_type=jtype,
                                                    posted_date=date))
        elif choice == "4":
            companies = admin_dao.get_companies()
            for c in companies:
                print(f"ID: {c.CompanyID} | Name: {c.CompanyName} | Location: {c.Location}")
        elif choice == "5":
            jobs = admin_dao.get_job_listings()
            for j in jobs:
                print(j)
        elif choice == "6":
            applicants = admin_dao.get_applicants()
            for a in applicants:
                print(a)
        elif choice == "7":
            job_id = int(input("Enter Job ID: "))
            applications = admin_dao.get_applications_for_job(job_id)
            for app in applications:
                print(app)
        elif choice == "8":
            break

# Applicant functionality
def applicant_menu():
    applicant_dao = ApplicantDAO()

    while True:
        print("\nApplicant Menu:")
        print("1. View All Job Listings")
        print("2. Create Profile")
        print("3. Apply for a Job")
        print("4. Search Jobs by Salary Range")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            applicant_dao.fetch_job_listings()
        elif choice == "2":
            email = input("Enter email: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number: ")
            resume = input("Enter resume file path: ")
            applicant_dao.create_applicant_profile(email, first_name, last_name, phone, resume)
        elif choice == "3":
            applicant_id = int(input("Enter Applicant ID: "))
            job_id = int(input("Enter Job ID: "))
            cover_letter = input("Enter cover letter: ")
            applicant_dao.apply_for_job(applicant_id, job_id, cover_letter)
        elif choice == "4":
            min_salary = float(input("Enter minimum salary: "))
            max_salary = float(input("Enter maximum salary: "))
            applicant_dao.salary_range_query(min_salary, max_salary)
        elif choice == "5":
            break


if __name__ == "__main__":
    print("=" * 60)
    print("🤝  Welcome to CareerHub Portal".center(60))
    print("=" * 60)
    print("Your gateway to finding the perfect job or top talent!\n")

    role = input("🔹 Are you logging in as an *Applicant* or *Admin*? (applicant/admin): ").strip().lower()

    if role == "admin":
        admin_menu()
    elif role == "applicant":
        applicant_menu()
    else:
        print("Invalid role.")
