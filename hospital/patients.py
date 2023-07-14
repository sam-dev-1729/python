from appointments import Appointment


class Patient:

    def __init__(self, name, age, address, phone, ID_number, sickness):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.ID_number = ID_number
        self.sickness = sickness
        self.appointment = []

    def book_appointment(self, patient, doctor, appointment_date, appointment_time):
        appointment = Appointment(patient, doctor, appointment_date, appointment_time)
        self.appointment.append(appointment)
        print("Appointment booked for {} on {} at {}".format(patient.name, appointment_date, appointment_time))