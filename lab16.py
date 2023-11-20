from abc import ABC, abstractmethod


# Агрегат (Aggregate)
class UniversityDepartment(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


# Конкретний агрегат (Concrete Aggregate)
class Faculty(UniversityDepartment):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def create_iterator(self):
        return FacultyIterator(self.students)


# Ітератор (Iterator)
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# Конкретний ітератор (Concrete Iterator)
class FacultyIterator(Iterator):
    def __init__(self, students):
        self.students = students
        self.index = 0

    def has_next(self):
        return self.index < len(self.students)

    def next(self):
        if self.has_next():
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


# Клас студента
class Student:
    def __init__(self, name):
        self.name = name


# Клієнтський код
if __name__ == "__main__":
    faculty = Faculty()
    faculty.add_student(Student("John Doe"))
    faculty.add_student(Student("Jane Doe"))
    faculty.add_student(Student("Bob Smith"))

    iterator = faculty.create_iterator()

    # Використання ітератора для ітерації по студентах
    while iterator.has_next():
        student = iterator.next()
        print(f"Student: {student.name}")
