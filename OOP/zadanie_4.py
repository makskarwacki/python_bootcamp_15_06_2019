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


class Discount:
    def __init__(self, amount):
        self.amount = amount

    def calculate(self, basket_total_price):
        return basket_total_price - self.amount


class ValueDiscount(Discount):

    def __add__(self, other):
        return ValueDiscount(self.amount + other.amount)


class PercentDiscount(Discount):

    def calculate(self, basket_total_price):
        if self.amount:
            return basket_total_price - basket_total_price * (self.amount / 100)
        return basket_total_price

    def __add__(self, other):
        return PercentDiscount(self.amount + other.amount)


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
        self.discounts = []

    def add_product(self, product: Product, quantity: int):
        """add basket entry to basket"""

        self.entries.append(BasketEntry(product, quantity))

    def add_discount(self, discount):
        self.discounts.append(discount)

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()

        temp_vd = ValueDiscount(0)
        temp_pd = PercentDiscount(0)
        for d in self.discounts:
            if isinstance(d, ValueDiscount):
                temp_vd += d
            elif isinstance(d, PercentDiscount):
                temp_pd += d

        total_price = temp_vd.calculate(total_price)
        total_price = temp_pd.calculate(total_price)

        return total_price

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for entry in self.entries:
            report += entry.generate_report()
        report += f"W sumie: {self.count_total_price():.2f}\n"
        return report

    @staticmethod
    def with_products(products_list):
        basket = Basket()
        for product in products_list:
            basket.add_product(product, 1)
        return basket


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

    def test_with_products(self):
        pr1 = Product("A", 10)
        pr2 = Product("B", 20)

        basket = Basket.with_products([pr1, pr2])

        assert len(basket.entries) == 2
        assert basket.entries[0].quantity == 1
        assert basket.entries[0].product.nazwa == "A"
        assert basket.entries[1].quantity == 1


    def test_add_discount(self):
        pr1 = Product("A", 10)
        pr2 = Product("B", 20)

        basket = Basket.with_products([pr1, pr2])
        assert basket.count_total_price() == 30

        vd1 = ValueDiscount(5)
        vd2 = ValueDiscount(5)
        pd1 = PercentDiscount(10)
        pd2 = PercentDiscount(10)

        basket.add_discount(vd1)
        basket.add_discount(vd2)
        basket.add_discount(pd1)
        basket.add_discount(pd2)

        assert basket.count_total_price() == 16
