from random import randint as rnd

REZ_X = 100
REZ_Y = 80


class Character:

    def __init__(self, name, energy, attack, defense, speed):
        self.name = name
        self.energy = energy
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.cure = 0 # --czy tak OK ?
        self.defence_level = 0 # --czy tak OK ?
        self.inventory = []

    def add_item(self, item):
        """dodaje obiekt Item do listy inventory"""
        self.inventory.append(item)

    def get_cure(self):
        """podnosi ilosc energii o x% w zależnosci od rodzaju postaci"""
        self.energy *= 1+(self.cure/100) # --czy tak OK ?

    def get_damage(self, value):
        """oblicza wartość otrzymanego obrażenia value=attack -- jeszcze do przemyslenia"""
        damage = value - rnd(int(self.defense*0.2),int(self.defense*self.defence_level))# -- raczej do poprawy
        if damage > 0 and self.energy > damage:
            self.energy-=damage
        else:
            self.energy-=value

    # @property
    # def




class Warrior(Character):
    def __init__(self, name, energy, attack, defense, speed):
        Character.__init__(self, name, energy, attack, defense, speed)
        self.cure = 35
        self.defence_level =0.6
        self.speciality = 'Warrior'


class Magnus(Character):
    def __init__(self, name, energy, attack, defense, speed):
        Character.__init__(self, name, energy, attack, defense, speed)
        self.cure = 60
        self.defence_level = 0.5
        self.speciality = 'Magnus'


class Barbarian(Character):
    def __init__(self, name, energy, attack, defense, speed):
        Character.__init__(self, name, energy, attack, defense, speed)
        self.cure = 20
        self.defence_level = 0.3
        self.speciality = 'Barbarian'


class Item:
    def __init__(self, name, energy_bonus, attack_bonus, defense_bonus, speed_bonus):
        self.name = name
        self.energy_bonus = energy_bonus
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.speed_bonus = speed_bonus

    def __str__(self):
        return f'''
Przedmiot| {self.name} 
Parametry| Energia:{self.energy_bonus} Atak:{self.attack_bonus} Obrona:{self.defense_bonus} Szybkość:{self.speed_bonus}
'''


class Location:

    def __init__(self, x, y, x_max=REZ_X, y_max=REZ_Y):
        self.x = x
        self.y = y
        self.x_max = x_max
        self.y_max = y_max

    # obliczamy odległość do innego obiektu (a.get_distance_to(b) zwraca odległość)
    def get_distance_to(self, position):
        return ((position.x - self.x) ** 2 + (position.y - self.y) ** 2) ** (1 / 2)

    # po wywołaniu na obiekcie zmienia losowo położenie
    def get_random_location(self):
        self.x = rnd(0, self.x_max)
        self.y = rnd(0, self.y_max)


"""
TODO: Poruszanie się
"""

person = Magnus('Mirek', 100, 20, 20, 20)
miecz = Item('miecz',10,25,10,-5)
tarcza = Item('tarcza',5,6,30,-3)
person.add_item(miecz)
person.add_item(tarcza)
print(person.inventory[0], person.inventory[1])
print(person.speciality, person.name,person.energy)
person.get_cure()
print(person.speciality, person.name,person.energy)

