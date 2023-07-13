        
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
class Doctor(Staff):
    
    def __init__(self, name, speciality):
        super().__init__(name, "Doctor")
        self.speciality = speciality
        
class Nurse(Staff):
    
    def __init__(self, name):
        super().__init__(name, "Nurse")