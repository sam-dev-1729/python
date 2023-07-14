class Staff:
    def __init__(self, name ,role):
        self.name = name
        self.role = role


class Doctor(Staff):

    def __init__(self, name, age, phone, address, speciality):
        super().__init__(name, "Doctor")
        self.age = age
        self.phone = phone
        self.address = address
        self.speciality = speciality


class Nurse(Staff):

    def __init__(self, name, age, phone, address):
        super().__init__(name, "Nurse")
        self.age = age
        self.phone = phone
        self.address = address


class Others(Staff):

    def __init__(self, name, age, phone, address):
        super().__init__(name, "Worker")
        self.age = age
        self.phone = phone
        self.address = address
