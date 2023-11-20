from abc import ABC, abstractmethod


# Контекст (Context)
class Student:
    def __init__(self, name):
        self.name = name
        self.state = NewStudentState()

    def change_state(self, new_state):
        self.state = new_state

    def request_info(self):
        self.state.handle_request(self)


# Стан (State)
class StudentState(ABC):
    @abstractmethod
    def handle_request(self, student):
        pass


# Конкретний стан (Concrete State)
class NewStudentState(StudentState):
    def handle_request(self, student):
        print(f"{student.name}, ви новий студент. Зверніться до відділу прийому.")


# Конкретний стан (Concrete State)
class EnrolledStudentState(StudentState):
    def handle_request(self, student):
        print(f"{student.name}, ви зараховані. Зверніться до відділу навчання.")


# Конкретний стан (Concrete State)
class GraduatedStudentState(StudentState):
    def handle_request(self, student):
        print(f"{student.name}, ви закінчили навчання. Вітаємо!")


# Клієнтський код
if __name__ == "__main__":
    student = Student("John")

    # Початковий стан: новий студент
    student.request_info()

    # Зміна стану на "зарахований"
    student.change_state(EnrolledStudentState())
    student.request_info()

    # Зміна стану на "закінчив навчання"
    student.change_state(GraduatedStudentState())
    student.request_info()
