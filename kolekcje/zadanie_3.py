lista = [1, 2, -10, 13, 17, -21, 23, 26]

liczby_dodatnie = 0
liczby_ujemne = 0

for liczba in lista:
    if liczba < 0:
        liczby_ujemne += 1
    else:
        liczby_dodatnie += 1
print(liczba)

print(f"""
Liczb dodatnich: {liczby_dodatnie}
Liczb ujemnych: {liczby_ujemne}
""")