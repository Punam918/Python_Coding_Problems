'''Write a Python program to create an instance of a specified class and display the namespace of the 
said instance.'''
class Student:
    def __init__(self,studentid,studentname,classname):
        self.studentid = studentid
        self.studentname = studentname
        self.classname = classname    
student = Student("062","punam","4th year")
print(student.__dict__)
