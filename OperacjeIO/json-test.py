import json

dict = { "imie" : "Jan", "nazwisko" : "Kowalski", "wiek" : 44, "motto" : "żażółć gęslą jaźń"  }

with open("json.txt", "wt") as f:
    s = json.dumps(dict, indent=4)
    #print(s)
    json.dump(dict, f)

with open("json.txt", "rt") as f:
    s = f.read()
    dict1 = json.loads(s)
    print(dict1)

