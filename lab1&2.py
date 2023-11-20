class Student:
    def __init__(self, name, surname, age, course, subjects):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course
        self.subjects = subjects

    def shallow_copy(self):
        return Student(self.name, self.surname, self.age, self.course, self.subjects)

    def deep_copy(self):
        student = Student(self.name, self.surname, self.age, self.course, [])
        if self.subjects:
            student.subjects = [subject.deep_copy() for subject in self.subjects]
        return student

    def __str__(self):
        result = f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Course: {self.course}, Subjects:"
        if self.subjects:
            for subject in self.subjects:
                result += subject.__str__()
        return result


class StudentDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StudentDatabase, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students


class Subject:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def deep_copy(self):
        return Subject(self.name, self.mark)

    def __str__(self):
        return f"\nName: {self.name}, Mark: {self.mark}"


# Subject instance
subjects = [Subject("Architecture", 100)]

# Creation of first instance of Singleton Database
student_db = StudentDatabase()

first_student = Student("Danyil", "Terentiev", 19, 3, subjects)
second_student = Student("Maksym", "Proskurniak", 20, 3, subjects)

student_db.add_student(first_student)

# Second instance even though that is the same object reference
student_db2 = StudentDatabase()
student_db2.add_student(second_student)

# Check whether the student_db2 has two records of students
for s in student_db2.get_all_students():
    print(s)

# Prototype Pattern
# Creating thirdStudent by using DeepCopy method
third_student = first_student.deep_copy()
# Altering subject object
third_student.subjects[0].name = "JAVA YIKES!!!"

print(f"First student - {first_student}")
print(f"Third student - {third_student}")
