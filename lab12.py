from typing import Dict


# Легковаговий об'єкт (Flyweight)
class Subject:
    def __init__(self, name):
        self.name = name


# Фабрика легковагових об'єктів
class SubjectFactory:
    _subjects: Dict[str, Subject] = {}

    @staticmethod
    def get_subject(name):
        if name not in SubjectFactory._subjects:
            SubjectFactory._subjects[name] = Subject(name)
        return SubjectFactory._subjects[name]


# Контекст
class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def display_subjects(self):
        print(f"Студент {self.name} вивчає предмети:")
        for subject in self.subjects:
            print(f"- {subject.name}")


# Клієнтський код
if __name__ == "__main__":
    subject_factory = SubjectFactory()

    math = subject_factory.get_subject("Математика")
    physics = subject_factory.get_subject("Фізика")
    programming = subject_factory.get_subject("Програмування")

    student1 = Student("John", [math, physics])
    student2 = Student("Jane", [math, programming])

    student1.display_subjects()
    print("---")
    student2.display_subjects()
