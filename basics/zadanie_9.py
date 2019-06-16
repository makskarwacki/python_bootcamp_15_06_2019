import datetime
current_year = datetime.datetime.now().year

# current_year = 2019
b_year = int(input("Podaj rok urodzenia: "))

if current_year - b_year >= 18:
    print("Jestes pełnoletni")
else:
    print("Musisz poczekać")