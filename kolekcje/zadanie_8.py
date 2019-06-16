
napis = "Ala ma <kota>, a kot ma Alę"

ile = 0
zliczaj = False

for i in napis:
    if i == "<":
        zliczaj = True
        continue
    elif i == ">":
        zliczaj = False
    if zliczaj:
        ile += 1

print(ile)
print(napis.index(">") - napis.index("<") - 1)
