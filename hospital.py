import random
from operator import itemgetter

class Patient(object):
    def __init__(self, id, name, allergies, bed_number = None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number


class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def admit(self, arg):
        if len(self.patients) <= self.capacity:
            self.patients.append(arg)
            for key in self.patients:
                key.bed_number = random.randint(1, 50)
            print "Patient: " + key.name + " approved"
            print vars(key)
        else:
            print "Sorry, hospital is full"
        return self
    
    def discharge(self, arg):
        for i in range(0, len(self.patients)):
                if arg == self.patients[i].name:
                    index_of_pop = i
                    print "Patient: " + self.patients[i].name + " discharged"
                    self.patients[i].bed_number = None
        self.patients.pop(index_of_pop)
        print self.patients
        return self

patient1 = Patient(1, "Bam", "Skateboards")
patient2 = Patient(2, "Elliot", "People")
print Hospital("Some Hospital", 2).admit(patient1).admit(patient2).admit(patient1).discharge("Elliot")
