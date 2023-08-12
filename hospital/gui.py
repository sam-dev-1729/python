#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.ttk as ttk
import tkcalendar

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
        self.appointments = []

class Patient:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.role = "Doctor"

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

# Initialize hospital
hospital = Hospital("City Hospital")

# Add sample data
patient1 = Patient("John Doe", "123 Main St", "555-1234")
patient2 = Patient("Jane Doe", "456 Park Ave", "555-5678")
doctor1 = Doctor("Dr. Smith", "Pediatrics")
doctor2 = Doctor("Dr. Johnson", "Orthopedics")
hospital.patients.append(patient1)
hospital.patients.append(patient2)
hospital.staff.append(doctor1)
hospital.staff.append(doctor2)

# Functions
def add_patient():
    # Get data
    name = patient_name.get()  
    address = patient_address.get()
    phone = patient_phone.get()
    
    # Validate
    if not name or not address or not phone:
        messagebox.showerror("Error", "Please fill out all fields")
        return
        
    # Create Patient object
    patient = Patient(name, address, phone)
    
    # Add to hospital list
    hospital.patients.append(patient)
    
    # Confirmation
    messagebox.showinfo("Success", f"{name} added as a patient")
    display_patients()
    
def display_patients():
    # Clear listbox
    patient_listbox.delete(0, tk.END)
    
    # Add patients to listbox
    for patient in hospital.patients:
        patient_listbox.insert(tk.END, patient.name)
        
def add_doctor():
    # Get data
    name = doctor_name.get()
    specialty = doctor_specialty.get()
    
    # Validate
    if not name or not specialty:
        messagebox.showerror("Error", "Please fill out all fields")
        return
    
    # Create Doctor object  
    doctor = Doctor(name, specialty)
    
    # Add to hospital staff list
    hospital.staff.append(doctor)
    
    # Confirmation
    messagebox.showinfo("Success", f"{name} added as a doctor")    
    display_doctors()

def display_doctors():
    # Clear listbox
    doctor_listbox.delete(0, tk.END)

    # Add doctors to listbox
    for doctor in hospital.staff:
        if doctor.role == "Doctor":
            doctor_listbox.insert(tk.END, doctor.name + ' - ' + doctor.specialty)
            
def book_appointment(patient_var, doctor_var):
    # Get data
    patient_name = patient_var.get()
    doctor_name = doctor_var.get()
    date = date_var.get()
    time = time_var.get()

    # Validate
    if not patient_name or not doctor_name or not date or not time:
        messagebox.showerror("Error", "Please fill out all fields")
        return
    
    # Get patient and doctor objects
    patient = get_patient(patient_name)
    doctor = get_doctor(doctor_name)
    
    # Validate patient and doctor
    if not patient or not doctor:
        messagebox.showerror("Error", "Invalid patient or doctor")
        return
    
    # Create appointment
    appointment = Appointment(patient, doctor, date, time)
    
    # Add to hospital appointments
    hospital.appointments.append(appointment)

    # Confirmation
    messagebox.showinfo("Success","Appointment booked")
    display_appointments()
    
def get_patient(name):
    for patient in hospital.patients:
        if patient.name == name:
            return patient
        
def get_doctor(name):
    for doctor in hospital.staff:
        if doctor.name == name and doctor.role == "Doctor":
            return doctor
            
def display_appointments():
    # Clear listbox
    appointments_listbox.delete(0, tk.END)
    
    # Add appointments
    for appointment in hospital.appointments:
        appointments_listbox.insert(tk.END, 
            appointment.date + " - " + appointment.time + " - " + 
            appointment.patient.name + " - Dr. " + appointment.doctor.name)

# GUI tkinter code 
root = tk.Tk()
root.title("Hospital Management System")

# Tabs
nb = ttk.Notebook(root)

# Patient tab
patient_tab = ttk.Frame(nb)
nb.add(patient_tab, text="Patients")

# Patient fields
patient_name = tk.StringVar()
patient_address = tk.StringVar()
patient_phone = tk.StringVar()

tk.Label(patient_tab, text="Name").grid(row=0, column=0)
tk.Entry(patient_tab, textvariable=patient_name).grid(row=0, column=1)

tk.Label(patient_tab, text="Address").grid(row=1, column=0)
tk.Entry(patient_tab, textvariable=patient_address).grid(row=1, column=1)

tk.Label(patient_tab, text="Phone").grid(row=2, column=0)  
tk.Entry(patient_tab, textvariable=patient_phone).grid(row=2, column=1)

tk.Button(patient_tab, text="Add Patient", command=add_patient).grid(row=3, column=0, columnspan=2)

# Patient listbox
patient_listbox = tk.Listbox(patient_tab)
patient_listbox.grid(row=4, column=0, columnspan=2)

# Doctor tab
doctor_tab = ttk.Frame(nb) 
nb.add(doctor_tab, text='Doctors')

# Doctor fields
doctor_name = tk.StringVar()
doctor_specialty = tk.StringVar()

tk.Label(doctor_tab, text="Name").grid(row=0, column=0)
tk.Entry(doctor_tab, textvariable=doctor_name).grid(row=0, column=1)

tk.Label(doctor_tab, text="Specialty").grid(row=1, column=0)
tk.Entry(doctor_tab, textvariable=doctor_specialty).grid(row=1, column=1)

tk.Button(doctor_tab, text="Add Doctor", command=add_doctor).grid(row=2, column=0, columnspan=2)

# Doctor listbox 
doctor_listbox = tk.Listbox(doctor_tab)
doctor_listbox.grid(row=3, column=0, columnspan=2)

# Appointments tab
appointments_tab = ttk.Frame(nb)
nb.add(appointments_tab, text='Appointments')

# Dropdowns
patient_var = tk.StringVar()
patient_dropdown = ttk.Combobox(appointments_tab, textvariable=patient_var)
patient_dropdown['values'] = [p.name for p in hospital.patients]
patient_dropdown.grid(row=0, column=0) 

doctor_var = tk.StringVar()
doctor_dropdown = ttk.Combobox(appointments_tab, textvariable=doctor_var)
doctor_dropdown['values'] = [d.name for d in hospital.staff if d.role=="Doctor"] 
doctor_dropdown.grid(row=0, column=1)

# Date and time fields
date_var = tk.StringVar()  
date_picker = tkcalendar.DateEntry(appointments_tab, textvariable=date_var)
date_picker.grid(row=1, column=0)

time_var = tk.StringVar() 
time_picker = ttk.Combobox(appointments_tab, width=15, textvariable=time_var)
time_picker['values'] = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
time_picker.grid(row=1, column=1) 

# Book appointment button
book_btn = ttk.Button(appointments_tab, text="Book Appointment", command=book_appointment(patient_var, doctor_var))
book_btn.grid(row=2, column=0, columnspan=2)  

# Appointments listbox
appointments_listbox = tk.Listbox(appointments_tab)
appointments_listbox.grid(row=3, column=0, columnspan=2)

# Display initial doctors and patients
display_patients()
display_doctors()

nb.pack(expand=True, fill='both')

root.mainloop()