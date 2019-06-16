a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
op = input("Podaj rodzaj operacji: ")

wynik = "Nieznana operacja"


if op == "+":
    wynik = a + b
elif op == "-":
    wynik = a - b
elif op == "*":
    wynik = a * b
elif op == "/":
    if b == 0:
        wynik = "Nie dziel przez zero"
    else:
        wynik = a / b
# else:
#     wynik = "Nieznana operacja"

print("Wyniki ", wynik)
