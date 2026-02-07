class memper:
    def __init__(self, first_name, middle_name, last_name):

       self.fname = first_name

       self.mname = middle_name

       self.lname = last_name

memper1 = memper("Ahmed", "Ali", "Mohamed")
memper2 = memper("Omar", "Hassan", "Khaled")
memper3 = memper("Youssef", "Mahmoud", "Salah")

def full_name(self):
    
    return f"{self.fname} {self.mname} {self.lname}"
memper.full_name = full_name
print(memper1.full_name())
print(memper2.full_name())  
print(memper3.full_name())

def name_with_title(self):

    return f"Mr. {self.fname} {self.mname} {self.lname}"
print(name_with_title(memper1))

# Student class
class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
s = Student("Ali", 15, 90)
print(s.name, s.mark)
print(s.name, s.mark)