from departments import Department
from patients import Patient
from staff import Staff


class Hospital:

    def __init__(self, name, address, phone, website):
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website
        self.department = []

    def add_department(self, name_of_department):
        self.department.append(name_of_department)

# Example usage        
my_hospital = Hospital("City Hospital")

john = Patient("John Doe", "123 Main St", "555-1234") 
my_hospital.add_patient(john)

mary = Doctor("Mary Smith", "Cardiology")
my_hospital.add_staff(mary)

my_hospital.book_appointment(john, mary, "2019-12-01", "10:00")