'''Write a Python function student_data () that will print the ID of a student (student_id). 
If the user passes an argument
student_name or student_class the function will print the student name and class. use kwargs.'''
def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
student_data(101)
student_data(102, student_name="Alice")
student_data(103, student_name="Bob", student_class="10th Grade")
