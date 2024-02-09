from classes.person import Person
#This is an absolute import

class Student(Person):

    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role)
        self.school_id = school_id  
        self.password = password
        
    def __repr__(self):
        return f"{super().__repr__()} | School ID: {self.school_id}, Password : {self.password}"
       #uses fancy method
alice = Student("alice", "5", "student", "21234324", "XXXXX")
print(alice)