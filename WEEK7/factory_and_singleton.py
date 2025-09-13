from abc import ABC, abstractmethod

# Product Interface (Abstract Base Class):
# Defines a standard interface for all payment processors. By using ABC, we ensure that every payment method implements the process_payment method, enforcing consistency across implementations.
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

# Concrete Products:
# Each class below represents a specific payment method and implements the PaymentProcessor interface.
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via PayPal"

class StripePayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via Stripe"

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via Credit Card"

class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via Bank Transfer"

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via CryptoPayment"

class GooglePayPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing {amount} via GooglePay"


# Factory:
# The PaymentFactory class creates instances of payment processors based on the provided method name. This separates object creation from usage, making it easy to add or modify payment methods without changing client code.
class PaymentFactory:
    def create(self, method: str) -> PaymentProcessor:
        method = method.lower()
        if method == "paypal":
            return PayPalPayment()
        if method == "stripe":
            return StripePayment()
        if method == "credit_card":
            return CreditCardPayment()
        if method == "banktransfer":
            return BankTransferPayment()
        if method == "cryptopayment":
            return CryptoPayment()
        if method == "googlepay":
            return GooglePayPayment()
        raise ValueError(f"Unknown payment method: {method}")


# Singleton Pattern:
# PaymentGateway is implemented as a Singleton, meaning only one instance exists during the application's lifetime. This is important for shared resources like payment gateways, ensuring consistent state and avoiding duplicate processing.
class PaymentGateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process(self, payment_method: str, amount: float) -> str:
        processor = PaymentFactory().create(payment_method)
        return processor.process_payment(amount)

    def checkout(self, payment_method: str, amount: float) -> str:
        # Acts as a client method to process a payment using the factory.
        processor = PaymentFactory().create(payment_method)
        return processor.process_payment(amount)


def main():
    print("Available payment methods: paypal, creditcard, banktransfer, cryptopayment, googlepay")
    method = input("Enter payment method: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    gateway = PaymentGateway()
    try:
        result = gateway.process(method, amount)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
