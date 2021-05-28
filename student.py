class Student:
    school="Akirachix"
    
    def __init__(self,name,age):
        # student1=Student(name="Celine",age=21)
        # student2=Student(name="Bitama"age=24)
        self.name=name
        self.age=age

    def speak(self):
        return f"Hello my name is {self.name} I am {self.age} years old and I love {self.school}"


      