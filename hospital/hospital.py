from patients  import Patient
from  staff import Doctor,Nurse,Staff
from appointments import Appointment
from surgery import Surgery

class Hospital:

    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
        self.appointments = []
        self.surgerys=[]
    
    def add_patient(self, patient):
        self.patients.append(patient)
        
    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def book_appointment(self, patient, doctor, appointment_date, appointment_time):
        appointment = Appointment(patient, doctor, appointment_date, appointment_time)
        self.appointments.append(appointment)
        print("Appointment booked for {} on {} at {}".format(patient.name, appointment_date, appointment_time))
        
    def surgery(self,patient,doctor,kind_of_surgery,cost_of_surgery):
        surgery= Surgery(kind_of_surgery,cost_of_surgery,doctor,patient)
        self.surgerys.append(surgery)
        print("Surgery done for {} by {} costs {}".format(patient.name,doctor.name,surgery.cost_of_surgery))
        
        
        
# Example usage        
my_hospital = Hospital("City Hospital")

john = Patient("John Doe", "123 Main St", "555-1234") 
my_hospital.add_patient(john)

mary = Doctor("Mary Smith", "Cardiology")
my_hospital.add_staff(mary)

my_hospital.book_appointment(john, mary, "2019-12-01", "10:00")

frank=Patient("frank","Zabol","++12345678")
my_hospital.surgery(frank,mary,"Heart",17500)
