from abc import ABC, abstractmethod


# Product interface (Abstract Base Class)
# Using ABC allows us to define a common interface for all payment processors.
# This ensures that all concrete payment classes implement the process_payment method.
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


# Concrete products
# Each class implements the PaymentProcessor interface for a specific payment method.
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via PayPal"

class StripePayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via Stripe"

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via Credit Card"


# Factory
# The factory class is responsible for creating instances of payment processors based on the method name.
# This decouples the client code from the concrete classes, making it easy to add new payment methods.
class PaymentFactory:
    def create(self, method: str) -> PaymentProcessor:
        method = method.lower()
        if method == "paypal":
            return PayPalPayment()
        if method == "stripe":
            return StripePayment()
        if method == "credit_card":
            return CreditCardPayment()
        raise ValueError(f"Unknown payment method: {method}")


# Client code
# The checkout function acts as the client, using the factory to get the right processor and process the payment.
def checkout(payment_method: str, amount: float) -> str:
    processor = PaymentFactory().create(payment_method)
    return processor.process_payment(amount)


def main():
    print("Available payment methods: paypal, stripe, credit_card")
    method = input("Enter payment method: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    try:
        result = checkout(method, amount)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
