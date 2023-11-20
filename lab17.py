from abc import ABC, abstractmethod


# Посередник (Mediator)
class UniversityMediator(ABC):
    @abstractmethod
    def register_colleague(self, colleague):
        pass

    @abstractmethod
    def send_message(self, colleague, message):
        pass


# Колега (Colleague)
class UniversityColleague(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass


# Конкретний посередник (Concrete Mediator)
class AdmissionsMediator(UniversityMediator):
    def __init__(self):
        self.colleagues = []

    def register_colleague(self, colleague):
        self.colleagues.append(colleague)

    def send_message(self, colleague, message):
        for c in self.colleagues:
            if c != colleague:
                c.receive_message(message)


# Конкретний колега (Concrete Colleague)
class Student(UniversityColleague):
    def send_message(self, message):
        print(f"{self.name} відправляє повідомлення: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} отримує повідомлення: {message}")


# Клієнтський код
if __name__ == "__main__":
    admissions_mediator = AdmissionsMediator()

    student1 = Student(admissions_mediator, "John")
    student2 = Student(admissions_mediator, "Jane")

    admissions_mediator.register_colleague(student1)
    admissions_mediator.register_colleague(student2)

    student1.send_message("Важлива інформація для всіх студентів")
