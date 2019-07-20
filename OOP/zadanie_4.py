class Product:
    id_ = 0

    def __init__(self, nazwa, cena, id=None):

        if id is not None:
            self.id = id
        else:
            Product.id_ += 1
            self.id = self.id_
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt \"{self.nazwa}\", id: {self.id}, cena: {self.cena} PLN")


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def generate_report(self):
        return f" - {self.product.nazwa} ({self.product.id}), cena: {self.product.cena:.2f} x {self.quantity}\n"

class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product: Product, quantity: int):
        """add basket entry to basket"""

        self.entries.append(BasketEntry(product, quantity))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for entry in self.entries:
            report += entry.generate_report()
        report += f"W sumie: {self.count_total_price():.2f}\n"
        return report

class TestProduct:

    def test_initialization(self):
        pr = Product(id=10, nazwa="woda", cena=10)
        assert pr.id == 10
        assert pr.nazwa == "woda"
        assert pr.cena == 10


class TestBasket:

    def test_initialization(self):
        basket = Basket()
        assert len(basket.entries) == 0

    def test_add_product(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.entries) == 1

    def test_count_total_price(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50

    def test_generate_report(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)

        expected = f"""Produkty w koszyku:
 - Woda ({product.id}), cena: 10.00 x 5
W sumie: 50.00
"""
        assert basket.generate_report() == expected
