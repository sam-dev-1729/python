# Hospital Manager
This creates basic classes to represent `patients`, `staff`, and    `appointments` at a `hospital`. The Hospital class keeps track of them and allows actions like booking appointments.

You would still need to add a lot more logic around patient records, scheduling, billing etc. But this is a starting point to model the core components of a hospital system with Python classes.
## Patient
The Patient class stores basic information like name, address and phone number.
## Staff
The Staff base class defines name and role, extended by `Doctor` and `Nurse` subclasses to add speciality and override role.

The Appointment class links together a Patient, Doctor and timing.

This allows the Hospital class to create objects representing people and appointments at the hospital. The relationships between the classes enable modeling a hospital system with **OOP**.
