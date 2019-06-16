min_l = None
max_l = None

while True:
    x = input("Wpisz liczbę lub k by zakończyć")
    if x == 'k':
        break
    x = int(x)
    if min_l is None or x < min_l:
        min_l = x
    if max_l is None or x > max_l:
        max_l = x

if min_l == None:
    print("Nie wprowadziłeś liczb")
else:
    print(f"""
Znalezione minimum to : {min_l} 
Znalezione maksimum to : {max_l} 
""")