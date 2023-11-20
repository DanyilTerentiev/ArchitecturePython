from abc import ABC, abstractmethod


# Елемент (Element)
class UniversityElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Конкретний елемент (Concrete Element)
class Student(UniversityElement):
    def accept(self, visitor):
        visitor.visit_student(self)


# Конкретний елемент (Concrete Element)
class Professor(UniversityElement):
    def accept(self, visitor):
        visitor.visit_professor(self)


# Відвідувач (Visitor)
class Visitor(ABC):
    @abstractmethod
    def visit_student(self, student):
        pass

    @abstractmethod
    def visit_professor(self, professor):
        pass


# Конкретний відвідувач (Concrete Visitor)
class InformationVisitor(Visitor):
    def visit_student(self, student):
        print(f"Отримана інформація про студента")

    def visit_professor(self, professor):
        print(f"Отримана інформація про професора")


# Конкретний відвідувач (Concrete Visitor)
class EnrollmentVisitor(Visitor):
    def visit_student(self, student):
        print(f"Оформлення заяви на вступ для студента")

    def visit_professor(self, professor):
        print(f"Оформлення заяви на прийом на роботу для професора")


# Клієнтський код
if __name__ == "__main__":
    elements = [Student(), Professor()]

    information_visitor = InformationVisitor()
    enrollment_visitor = EnrollmentVisitor()

    print("Отримання інформації:")
    for element in elements:
        element.accept(information_visitor)

    print("\nОформлення заяв на вступ або прийом на роботу:")
    for element in elements:
        element.accept(enrollment_visitor)
