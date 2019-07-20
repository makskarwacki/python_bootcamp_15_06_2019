
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


woda = Product("Woda", 2.99, 10)
piwo = Product("Piwo", 3.00)

woda.print_info()
piwo.print_info()


