# Підсистема 1
class AdmissionOffice:
    def check_application(self):
        print("Перевірка заяви на вступ")


# Підсистема 2
class TuitionOffice:
    def process_payment(self):
        print("Обробка оплати навчання")


# Підсистема 3
class EnrollmentOffice:
    def enroll_student(self):
        print("Зачислення студента")


# Фасад
class UniversityFacade:
    def __init__(self):
        self.admission_office = AdmissionOffice()
        self.tuition_office = TuitionOffice()
        self.enrollment_office = EnrollmentOffice()

    def complete_admission_process(self):
        print("Початок процесу вступу")
        self.admission_office.check_application()
        self.tuition_office.process_payment()
        self.enrollment_office.enroll_student()
        print("Процес вступу завершено")


# Клієнтський код
if __name__ == "__main__":
    university_facade = UniversityFacade()

    # Студент подає заяву та оплачує навчання
    university_facade.complete_admission_process()
