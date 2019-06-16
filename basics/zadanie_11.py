x = int(input("Podaj X:"))
y = int(input("Podaj Y:"))

if x < 0 or x > 100 or y < 0 or y > 100:
    pozycja = "poza planszą"
elif x > 90 and y > 90:
    pozycja = "PG"
elif x > 90 and y > 10:
    pozycja = "PD"
elif x < 10 and y < 10:
    pozycja = "LD"
elif x < 10 and y > 90:
    pozycja = "LG"
elif x > 90:
    pozycja = "PK"
elif x < 10:
    pozycja = "LK"
elif y < 10:
    pozycja = "DK"
elif y > 90:
    pozycja = "GK"
else:
    pozycja = "C"

print(f"Gracz znajduje się w {pozycja}")