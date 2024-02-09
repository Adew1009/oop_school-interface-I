from classes.person import Person
#This is an absolute import

class Staff(Person):

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role)
        self.employee_id = employee_id  
        self.password = password
        
    def __repr__(self):
        return f"{super().__repr__()} | employee ID: {self.employee_id}, Password : {self.password}"
       #uses fancy method of calling parent repr
    

# alice = Staff("alice", "5", "student", "21234324", "XXXXX")
# print(alice)