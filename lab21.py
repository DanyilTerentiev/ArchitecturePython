from abc import ABC, abstractmethod


# Контекст (Context)
class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)


# Інтерфейс стратегії (Strategy)
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Конкретна стратегія (Concrete Strategy)
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата за навчання: {amount} грн кредитною карткою")


# Конкретна стратегія (Concrete Strategy)
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата за навчання: {amount} грн через PayPal")


# Конкретна стратегія (Concrete Strategy)
class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата за навчання: {amount} грн банківським переказом")


# Клієнтський код
if __name__ == "__main__":
    # Клієнт обирає стратегію оплати (може використовувати фабрику стратегій)
    credit_card_strategy = CreditCardPayment()
    paypal_strategy = PayPalPayment()
    bank_transfer_strategy = BankTransferPayment()

    # Контекст зазначає обрану стратегію
    context = PaymentContext(credit_card_strategy)

    # Виклик стратегії для здійснення оплати
    context.execute_payment(100)

    # Зміна стратегії під час виконання
    context.strategy = paypal_strategy
    context.execute_payment(50)

    # Ще зміна стратегії
    context.strategy = bank_transfer_strategy
    context.execute_payment(200)
