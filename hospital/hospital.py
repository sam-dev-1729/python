from patients  import Patient
from  staff import Doctor,Nurse,Staff
from appointments import Appointment

class Hospital:

    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
        self.appointments = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
        
    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def book_appointment(self, patient, doctor, appointment_date, appointment_time):
        appointment = Appointment(patient, doctor, appointment_date, appointment_time)
        self.appointments.append(appointment)
        print("Appointment booked for {} on {} at {}".format(patient.name, appointment_date, appointment_time))
        
# Example usage        
my_hospital = Hospital("City Hospital")

john = Patient("John Doe", "123 Main St", "555-1234") 
my_hospital.add_patient(john)

mary = Doctor("Mary Smith", "Cardiology")
my_hospital.add_staff(mary)

my_hospital.book_appointment(john, mary, "2019-12-01", "10:00")