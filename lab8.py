from typing import Protocol


# Интерфейс ITakeClasses
class ITakeClasses(Protocol):
    def take_class(self):
        ...

    def do_practical(self):
        ...


# Реализация ArchitectureClass
class ArchitectureClass(ITakeClasses):
    def take_class(self):
        print("Learning about World of Warcraft with aid of an abstract factory!")

    def do_practical(self):
        print("Realising that adapter, proxy, decorator, and bridge use the same concept of composition!")


# Реализация DotNetClass
class DotNetClass(ITakeClasses):
    def take_class(self):
        print("Sit just for a minute turns into a long hour and a half")

    def do_practical(self):
        print("Failing to complete one practical assignment in one class")


# Абстрактный класс Student
class Student:
    def __init__(self, take_classes: ITakeClasses, first_name: str, last_name: str):
        self.take_classes = take_classes
        self.first_name = first_name
        self.last_name = last_name

    def learn(self):
        print(f"{self.first_name} {self.last_name} learns")
        self.take_classes.take_class()
        self.take_classes.do_practical()


# Конкретная реализация DmytroHutsuliak
class DmytroHutsuliak(Student):
    def learn(self):
        print("П'є терновецьке у пившнюсі")
        super().learn()


# Конкретная реализация TarasykHavrylets
class TarasykHavrylets(Student):
    def learn(self):
        print("Learns dev ops")
        self.take_classes.take_class()


# Использование классов и интерфейсов
classes = ArchitectureClass()

dima_hutsuliak = DmytroHutsuliak(classes, "Dima", "Hutsuliak")
dima_hutsuliak.learn()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    classes = ArchitectureClass()

    dima_hutsuliak = DmytroHutsuliak(classes, "Dima", "Hutsuliak")
    dima_hutsuliak.learn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
