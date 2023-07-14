from patients import Patient
from staff import Doctor
class Surgery(Patient,Doctor):
    def __init__(self,kind_of_surgery,cost_of_surgery,doctor,patient):
        self.kind_of_surgery=kind_of_surgery
        self.cost_of_surgery=cost_of_surgery
        self.doctor=doctor
        self.patient=patient
        
def surgery(self,patient,doctor,kind_of_surgery,cost_of_surgery):
        surgery= Surgery(kind_of_surgery,cost_of_surgery,doctor,patient)
        self.surgerys.append(surgery)
        print("Surgery done for {} by {} costs {}".format(patient.name,doctor.name,surgery.cost_of_surgery))


        
    
