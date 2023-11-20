class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def create_memento(self):
        return StudentMemento(self.name, self.age)

    def restore_memento(self, memento):
        self.name = memento.name
        self.age = memento.age

    def display_information(self):
        print(f"Student: {self.name}, Age: {self.age}")


class StudentMemento:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentCaretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


if __name__ == "__main__":
    student = Student("John", 20)
    student.display_information()

    caretaker = StudentCaretaker()

    # Збереження стану студента
    caretaker.add_memento(student.create_memento())

    # Зміна стану студента
    student.name = "John Doe"
    student.age = 21
    student.display_information()

    # Відновлення попереднього стану
    previous_state = caretaker.get_memento(0)
    student.restore_memento(previous_state)
    student.display_information()
