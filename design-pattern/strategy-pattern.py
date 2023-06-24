from abc import ABCMeta, abstractmethod


class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount):
        pass


class NaverPay(PaymentStrategy):
    def __init__(self, name, card_number, cvv, expire_date):
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.expire_date = expire_date

    def pay(self, amount):
        print(f"NaverPay로 {amount}원 결제합니다.")


class GooglePay(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"GooglePay로 {amount}원 결제합니다.")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def pay(self, payment_method: PaymentStrategy):
        amount = self.calculate_total()
        payment_method.pay(amount)


cart = ShoppingCart()
cart.add_item(Item("Macbook Pro 14", 2600000))
cart.add_item(Item("Vamilo Keyboard", 180000))

cart.pay(NaverPay("lululu", "1234-1234-1234-1234", "123", "12/24"))
cart.pay(GooglePay("luvel@gmail.com", "123456789"))
