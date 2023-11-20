from abc import ABC, abstractmethod


# Об'єкт запиту
class Request:
    def __init__(self, type, content):
        self.type = type
        self.content = content


# Базовий обробник (Handler)
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass


# Конкретний обробник (Concrete Handler)
class AdmissionHandler(Handler):
    def handle_request(self, request):
        if request.type == "Admission":
            print(f"AdmissionHandler обробляє запит: {request.content}")
        elif self.successor is not None:
            self.successor.handle_request(request)


# Конкретний обробник (Concrete Handler)
class PaymentHandler(Handler):
    def handle_request(self, request):
        if request.type == "Payment":
            print(f"PaymentHandler обробляє запит: {request.content}")
        elif self.successor is not None:
            self.successor.handle_request(request)


# Конкретний обробник (Concrete Handler)
class EnrollmentHandler(Handler):
    def handle_request(self, request):
        if request.type == "Enrollment":
            print(f"EnrollmentHandler обробляє запит: {request.content}")
        elif self.successor is not None:
            self.successor.handle_request(request)


# Клієнтський код
if __name__ == "__main__":
    # Створення ланцюжка відповідальності
    admission_handler = AdmissionHandler()
    payment_handler = PaymentHandler(admission_handler)
    enrollment_handler = EnrollmentHandler(payment_handler)

    # Створення та обробка запитів
    request1 = Request("Admission", "Запит на вступ")
    enrollment_handler.handle_request(request1)

    print("---")

    request2 = Request("Payment", "Запит на оплату")
    enrollment_handler.handle_request(request2)

    print("---")

    request3 = Request("Other", "Інший запит")
    enrollment_handler.handle_request(request3)
