from abc import ABC, abstractmethod


# Команда (Command)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретна команда (Concrete Command)
class AdmissionCommand(Command):
    def __init__(self, admission_office):
        self.admission_office = admission_office

    def execute(self):
        self.admission_office.process_admission()


# Конкретна команда (Concrete Command)
class PaymentCommand(Command):
    def __init__(self, tuition_office):
        self.tuition_office = tuition_office

    def execute(self):
        self.tuition_office.process_payment()


# Виконавець (Receiver)
class AdmissionOffice:
    def process_admission(self):
        print("Відділ прийому обробляє вступ")


# Виконавець (Receiver)
class TuitionOffice:
    def process_payment(self):
        print("Відділ оплати обробляє оплату")


# Викликач (Invoker)
class UniversityInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


# Клієнтський код
if __name__ == "__main__":
    admission_office = AdmissionOffice()
    tuition_office = TuitionOffice()

    admission_command = AdmissionCommand(admission_office)
    payment_command = PaymentCommand(tuition_office)

    invoker = UniversityInvoker()

    # Встановлення та виконання команд
    invoker.set_command(admission_command)
    invoker.execute_command()

    print("---")

    invoker.set_command(payment_command)
    invoker.execute_command()
