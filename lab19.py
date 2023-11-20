from abc import ABC, abstractmethod


# Інтерфейс спостерігача (Observer)
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Конкретний спостерігач (Concrete Observer)
class Student(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} отримав повідомлення: {message}")


# Суб'єкт (Subject)
class UniversityAnnouncement:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def make_announcement(self, announcement):
        print(f"Університет оголошує: {announcement}")
        self.notify_observers(announcement)


# Клієнтський код
if __name__ == "__main__":
    university_announcement = UniversityAnnouncement()

    student1 = Student("John")
    student2 = Student("Jane")

    university_announcement.add_observer(student1)
    university_announcement.add_observer(student2)

    university_announcement.make_announcement("Заняття перенесено на завтра")
