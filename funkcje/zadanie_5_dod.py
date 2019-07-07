"""

Napisz funkcję, która sprawdzi, czy napis jest pangramem

"""

import string

print(string.ascii_lowercase + "ąćęłńśźżó")

def is_pangram(text, letters=string.ascii_lowercase):

    text = text.lower()
    for znak in set(text):
        if znak not in letters:
            text = text.replace(znak, "")

    print(len(set(text)))
    if len(set(text)) < len(letters):
        return False
    return True

polish_letters = letters=string.ascii_lowercase.replace("x", "").replace("v", "").replace("q", "") + "ąćęłńśźżó"
print(len(polish_letters))

def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram("Ala ma kota") == False
    assert is_pangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig.", letters=polish_letters) == True
