from patients import Patient
from staff import Staff

class Department:

    def __init__(self, name, floor, names_of_staff, names_of_patients):
        self.name = name
        self.floor = floor
        self.names_of_staff = []
        self.names_of_patients = []

    def add_patient(self, patient):
        self.names_of_patients.append(patient)

    def add_staff(self, staff_member):
        self.names_of_staff.append(staff_member)