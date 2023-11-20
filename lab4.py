# Abstract classes for students and teachers
class Person:
    def __init__(self):
        self.name = None
        self.age = 0


class Student(Person):
    def __init__(self):
        super().__init__()
        self.major = None


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.department = None


# Abstract factory for creating students and teachers
class UniversityFactory:
    def create_student(self):
        pass

    def create_teacher(self):
        pass


# Concrete factory for creating students and teachers in the arts field
class ArtsUniversityFactory(UniversityFactory):
    def create_student(self):
        student = Student()
        student.major = "Fine Arts"
        return student

    def create_teacher(self):
        teacher = Teacher()
        teacher.department = "Art History"
        return teacher


# Concrete factory for creating students and teachers in the science field
class ScienceUniversityFactory(UniversityFactory):
    def create_student(self):
        student = Student()
        student.major = "Computer Science"
        return student

    def create_teacher(self):
        teacher = Teacher()
        teacher.department = "Physics"
        return teacher


def main():
    university_factory = None

    # Choose a factory to create students and teachers in the arts field
    university_factory = ArtsUniversityFactory()

    arts_student = university_factory.create_student()
    arts_teacher = university_factory.create_teacher()

    print(f"Student in Arts University: Major - {arts_student.major}")
    print(f"Teacher in Arts University: Department - {arts_teacher.department}")

    # Choose a factory to create students and teachers in the science field
    university_factory = ScienceUniversityFactory()

    science_student = university_factory.create_student()
    science_teacher = university_factory.create_teacher()

    print(f"Student in Science University: Major - {science_student.major}")
    print(f"Teacher in Science University: Department - {science_teacher.department}")


if __name__ == "__main__":
    main()
