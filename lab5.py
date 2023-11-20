# Клас, який представляє об'єкт, який ми будуємо
class UniversityApplication:
    def __init__(self):
        self.name = None
        self.age = None
        self.program = None
        self.documents = []

    def display(self):
        print(
            f"Application Details: Name: {self.name}, Age: {self.age}, Program: {self.program}, Documents: {self.documents}")


# Будівельник (Builder) - інтерфейс для створення об'єкта
class UniversityApplicationBuilder:
    def build_application(self):
        pass

    def set_name(self, name):
        pass

    def set_age(self, age):
        pass

    def set_program(self, program):
        pass

    def add_document(self, document):
        pass


# Конкретний будівельник (Concrete Builder)
class MedicalSchoolApplicationBuilder(UniversityApplicationBuilder):
    def __init__(self):
        self.application = UniversityApplication()

    def build_application(self):
        return self.application

    def set_name(self, name):
        self.application.name = name

    def set_age(self, age):
        self.application.age = age

    def set_program(self, program):
        self.application.program = f"Medical School - {program}"

    def add_document(self, document):
        self.application.documents.append(f"Medical Document: {document}")


# Конкретний будівельник (Concrete Builder)
class EngineeringSchoolApplicationBuilder(UniversityApplicationBuilder):
    def __init__(self):
        self.application = UniversityApplication()

    def build_application(self):
        return self.application

    def set_name(self, name):
        self.application.name = name

    def set_age(self, age):
        self.application.age = age

    def set_program(self, program):
        self.application.program = f"Engineering School - {program}"

    def add_document(self, document):
        self.application.documents.append(f"Engineering Document: {document}")


# Директор (Director) - відповідає за використання будівельника для створення об'єкта
class UniversityApplicationDirector:
    def construct_application(self, builder, name, age, program, documents):
        builder.set_name(name)
        builder.set_age(age)
        builder.set_program(program)
        for document in documents:
            builder.add_document(document)


# Клієнтський код
if __name__ == "__main__":
    # Створюємо будівельник для медичного факультету
    medical_builder = MedicalSchoolApplicationBuilder()

    # Створюємо директора
    director = UniversityApplicationDirector()

    # Клієнт викликає директора для побудови заяви для медичного факультету
    director.construct_application(medical_builder, "John Doe", 25, "Surgery", ["Transcript", "Recommendation Letter"])

    # Отримуємо готовий об'єкт
    medical_application = medical_builder.build_application()

    # Виводимо інформацію про заяву
    medical_application.display()
