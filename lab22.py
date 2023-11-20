from abc import ABC, abstractmethod


# Абстрактний клас, що визначає шаблонний метод
class UniversityAdmission(ABC):
    def admission_process(self):
        self.fill_application_form()
        self.submit_documents()
        self.perform_interview()
        self.get_admission_result()

    @abstractmethod
    def fill_application_form(self):
        pass

    @abstractmethod
    def submit_documents(self):
        pass

    @abstractmethod
    def perform_interview(self):
        pass

    @abstractmethod
    def get_admission_result(self):
        pass


# Конкретний клас, який реалізує шаблонний метод
class MedicalSchoolAdmission(UniversityAdmission):
    def fill_application_form(self):
        print("Заповнення анкети для медичного факультету")

    def submit_documents(self):
        print("Подання документів для медичного факультету")

    def perform_interview(self):
        print("Проведення співбесіди для медичного факультету")

    def get_admission_result(self):
        print("Отримання результату вступу на медичний факультет")


# Конкретний клас, який реалізує шаблонний метод
class EngineeringSchoolAdmission(UniversityAdmission):
    def fill_application_form(self):
        print("Заповнення анкети для інженерного факультету")

    def submit_documents(self):
        print("Подання документів для інженерного факультету")

    def perform_interview(self):
        print("Проведення співбесіди для інженерного факультету")

    def get_admission_result(self):
        print("Отримання результату вступу на інженерний факультет")


# Клієнтський код
if __name__ == "__main__":
    medical_school_admission = MedicalSchoolAdmission()
    engineering_school_admission = EngineeringSchoolAdmission()

    print("Процес вступу на медичний факультет:")
    medical_school_admission.admission_process()

    print("\nПроцес вступу на інженерний факультет:")
    engineering_school_admission.admission_process()
