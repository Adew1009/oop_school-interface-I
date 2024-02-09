from classes.school import School 
from classes.student import Student
from classes.staff import Staff
#This is an absolute import /  could also do .school import School


school = School('Ridgemont High') 

print(school.name)

alice = Student("alice", "5", "student", "21234324", "XXXXX")
print(alice)
bob = Staff("bob", "5", "teacher", "21234324", "XXXXX")
print(bob)

# New line