"""
Utwórz klasę Postac reprezentującą postać gracza.Ma atrybuty imie, zdrowie, max_zdrowie, atak i ekwipunekUtwórz klasę Przedmiot, który ma atrybuty nazwa, bonus_do_ataku
Jeśli przedmiot będzie w ekwipunku, to powiększa atak użytkownikaZmodyfikuj metodę __str__ która będzie przedstawiać użytkonika: npJestem Rufus, mam 35 ataku i 100/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do atakuPostać powinna mieć metody:otrzymaj_obrazenia - pomniejsza zdrowie o podaną wartość
wylecz - powieksza zdrowie o podaną wartość (do max_zdrowie)
daj_przedmiot  - dodaje przedmiot do ekwipunku
zabierz_przedmiot - usuwa przedmiot z ekwipunku
czy_zyje - jeśli zdrowie > 0 to żyje
moc_atakuZdefiniuj funkcję walkaWalka toczy się na śmierć i życie. Przeciwnicy walczą dopóki żyją.walka odbywa się pomiędzy atakującym i broniącym, którzy uderzają się na przemian.
Przed każdym uderzeniem wyliczana jest moc_ataku, która jest losową liczbą z zakresu od 0.5 atak do atakPrzykłdowa walka:Walka: Rufus vs Janusz



Jestem Rufus, mam 35 ataku i 100/100 życia.
EKWPIUNEK: Zielony tuplian zniszczenia, 5 do ataku

Jestem Janusz, mam 40 ataku i 120/120 życia.
EKWPIUNEK:

Rufus uderza Janusz za 35 obrażeń.
Janusz oberwał za 35 obrażeń.

Janusz uderza Rufus za 30 obrażeń.
Rufus oberwał za 30 obrażeń.

Jestem Rufus, mam 35 ataku i 70/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do atakuJestem Janusz, mam 40 ataku i 85/120 życia.
EKWPIUNEK:Rufus uderza Janusz za 18 obrażeń.
Janusz oberwał za 18 obrażeń.
Janusz uderza Rufus za 24 obrażeń.
Rufus oberwał za 24 obrażeń.
Jestem Rufus, mam 35 ataku i 46/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do atakuJestem Janusz, mam 40 ataku i 67/120 życia.
EKWPIUNEK:Rufus uderza Janusz za 33 obrażeń.
Janusz oberwał za 33 obrażeń.
Janusz uderza Rufus za 35 obrażeń.
Rufus oberwał za 35 obrażeń.
Jestem Rufus, mam 35 ataku i 11/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do atakuJestem Janusz, mam 40 ataku i 34/120 życia.
EKWPIUNEK:Rufus uderza Janusz za 34 obrażeń.
Janusz oberwał za 34 obrażeń.
Janusz uderza Rufus za 20 obrażeń.
Rufus oberwał za 20 obrażeń.

KONIEC WALKI

Jestem Rufus, miałem 35 i nie żyję.
Jestem Janusz, miałem 40 i nie żyję
"""

import random

class Hero:

    def __init__(self, name, attack, defense, energy):
        self.name = name
        self._attack = attack
        self._defense = defense
        self.energy = energy
        self.equipment = []

    def __str__(self):
        if self.energy <= 0:
            return f"{self.name} is dead!!"
        result = f"""{self.name} (A: {self.attack} | D: {self.defense} | E: {self.energy})
Equipment: 
"""
        for item in self.equipment:
            result += str(item)
        return result

    def add_item(self, item):
        self.equipment.append(item)

    @property
    def attack(self):
        result = self._attack
        for item in self.equipment:
            result += item.attack_bonus
        return result

    @property
    def defense(self):
        result = self._defense
        for item in self.equipment:
            result += item.defense_bonus
        return result

    def get_damage(self, value):
        damage = value - random.randint(1, self.defense // 2)
        if damage > 0:
            self.energy -= damage
            print(f"{self.name} oberwał za {damage}")

    @staticmethod
    def fight(hero_a, hero_d):

        while hero_a.energy > 0 and hero_d.energy > 0:
            hero_d.get_damage(hero_a.attack)
            if hero_d.energy > 0:
                hero_a.get_damage(hero_d.attack)

        print(hero_a)
        print(hero_d)

class Item:

    def __init__(self, name, attack_bonus, defense_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __str__(self):
        return f"{self.name} A: {self.attack_bonus} | D: {self.defense_bonus}\n"

class Location:

    def __init__(self, x, y, max_x=10, max_y=10):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def up(self):
        self.y += 1
        if self.y > self.max_y:
            raise ValueError("Wylecałeś poza planszę")

    def down(self):
        self.y -= 1
        if self.y < 1:
            raise ValueError("Wylecałeś poza planszę")

    def right(self):
        self.x += 1
        if self.x > self.max_x:
            raise ValueError("Wylecałeś poza planszę")

    def left(self):
        self.x -= 1
        if self.x < 1:
            raise ValueError("Wylecałeś poza planszę")

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

class Board:

    def __init__(self, gamer, enemy, item, x=10, y=10):
        """x, y - wymiary planszy"""
        self.gamer = gamer
        self.enemy = enemy
        self.item = item
        self.gamer_location = Location(random.randint(1, 10), random.randint(1, 10), x, y)
        self.enemy_location = Location(random.randint(1, 10), random.randint(1, 10), x, y)
        self.item_location = Location(random.randint(1, 10), random.randint(1, 10), x, y)

    def move(self):
        print(f'Twoja pozycja: {self.gamer_location}')
        print(f'Pozycja rzeczy: {self.item_location}')
        print(f'Pozycja wroga: {self.enemy_location}')
        direction = input("Podaj kierunek: w (góra) a (lewo) s (dół) d (prawo)")

        # if direction == "w":
        #     self.gamer_location.up()
        # elif direction == "a":
        #     self.gamer_location.left()
        # elif direction == "s":
        #     self.gamer_location.down()
        # elif direction == "d":
        #     self.gamer_location.right()

        # alternatywne rozwiązanie

        # direction_options = {
        #     "w": self.gamer_location.up,
        #     "a": self.gamer_location.left,
        #     "s": self.gamer_location.down,
        #     "d": self.gamer_location.right,
        # }
        #
        # direction_options[direction]()

        # alternatywne 2

        direction_options = {
            "w": "up",
            "a": "left",
            "s": "down",
            "d": "right",

        }

        method = direction_options[direction]
        getattr(self.gamer_location, method)()

        if self.gamer_location == self.item_location:
            print(f"Gracz znalazł przedmiot: {self.item}")
            self.gamer.add_item(self.item)

        if self.gamer_location == self.enemy_location:
            print(self.gamer)
            print(self.enemy)
            Hero.fight(self.gamer, self.enemy)

        if self.gamer.energy < 0:
            raise Exception("End game")

    def run(self):
        while True:
            try:
                self.move()
            except:
                print("Gra zakonczona")
                break

class TestItem:
    def test_item_initialization(self):
        item = Item("Siekiera", attack_bonus=50, defense_bonus=10)
        assert item.name == "Siekiera"
        assert item.attack_bonus == 50
        assert item.defense_bonus == 10

    def test_item_str(self):
        item = Item("Siekiera", attack_bonus=50, defense_bonus=10)
        assert str(item) == "Siekiera A: 50 | D: 10\n"

class TestHero:

    def test_postac_initialization(self):
        postac = Hero("Albert", attack=10, defense=10, energy=100)
        assert postac.name == "Albert"
        assert postac.attack == 10
        assert postac.defense == 10
        assert postac.energy == 100
        assert len(postac.equipment) == 0

    def test_postac_str(self):
        postac = Hero("Albert", attack=10, defense=10, energy=100)
        expected = """Albert (A: 10 | D: 10 | E: 100)
Equipment: 
"""
        assert str(postac) == expected
        postac = Hero("Albert", attack=10, defense=10, energy=0)
        expected = """Albert is dead!!"""
        assert str(postac) == expected

    def test_hero_with_item_str(self):
        hero = Hero("Albert", attack=10, defense=10, energy=100)
        item = Item("Siekiera", 50, 10)
        item2 = Item("Tarcza", 10, 50)
        hero.add_item(item)
        hero.add_item(item2)

        expected =  """Albert (A: 70 | D: 70 | E: 100)
Equipment: 
Siekiera A: 50 | D: 10
Tarcza A: 10 | D: 50
"""
        assert str(hero) == expected

    def test_add_item(self):
        postac = Hero("Albert", attack=10, defense=10, energy=100)
        assert postac.name == "Albert"
        assert postac.attack == 10
        assert postac.defense == 10
        assert postac.energy == 100
        assert len(postac.equipment) == 0
        siekiera = Item("Siekiera", 50, 10)
        postac.add_item(siekiera)
        assert len(postac.equipment) == 1
        assert postac.attack == 10 + 50
        assert postac.defense == 10 + 10
        assert postac.energy == 100

    def test_hero_get_damage(self):
        postac = Hero("Albert", attack=10, defense=10, energy=100)
        postac.get_damage(10)
        assert postac.energy < 100

#
adam = Hero("Adam", 10, 10, 100)
anna = Hero("Anna", 10, 10, 100)
item = Item("Axe", 40, 10)

board = Board(adam, anna, item)
board.run()