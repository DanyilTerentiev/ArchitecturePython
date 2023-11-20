from abc import ABC, abstractmethod


# Компонент (Component)
class UniversityComponent(ABC):
    @abstractmethod
    def display(self):
        pass


# Конкретний компонент (Concrete Component)
class BasicStudent(UniversityComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Базовий студент: {self.name}")


# Декоратор (Decorator)
class StudentDecorator(UniversityComponent, ABC):
    def __init__(self, student):
        self.student = student

    @abstractmethod
    def display(self):
        pass


# Конкретний декоратор (Concrete Decorator)
class HonorStudentDecorator(StudentDecorator):
    def display(self):
        print(f"Honor Student: {self.student.name}")


# Конкретний декоратор (Concrete Decorator)
class SportsStudentDecorator(StudentDecorator):
    def __init__(self, student, sport):
        super().__init__(student)
        self.sport = sport

    def display(self):
        print(f"Sports Student ({self.sport}): {self.student.name}")


# Клієнтський код
if __name__ == "__main__":
    basic_student = BasicStudent("John Doe")
    honor_student = HonorStudentDecorator(basic_student)
    sports_student = SportsStudentDecorator(basic_student, "Football")

    basic_student.display()
    print("---")
    honor_student.display()
    print("---")
    sports_student.display()
