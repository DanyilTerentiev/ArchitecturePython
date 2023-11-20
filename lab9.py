from abc import ABC, abstractmethod


# Компонент (Component)
class UniversityComponent(ABC):
    @abstractmethod
    def display(self):
        pass


# Конкретний компонент (Leaf)
class StudentLeaf(UniversityComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Студент: {self.name}")


# Компоновщик (Composite)
class DepartmentComposite(UniversityComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Факультет або кафедра: {self.name}")
        for child in self.children:
            child.display()


# Клієнтський код
if __name__ == "__main__":
    computer_science = DepartmentComposite("Комп'ютерні науки")
    physics = DepartmentComposite("Фізика")

    john = StudentLeaf("John Doe")
    jane = StudentLeaf("Jane Doe")

    computer_science.add(john)
    physics.add(jane)

    faculty = DepartmentComposite("Факультет наук")
    faculty.add(computer_science)
    faculty.add(physics)

    faculty.display()
