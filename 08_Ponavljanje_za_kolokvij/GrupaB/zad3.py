'''
Napisati regex za validaciju unešene lozinke.

Lozinka mora sadržavati:
Veliko slovo
Broj
Specijalni znak
Biti duža od 8 znakova
'''
import re

unos = input("Unesite lozinku:")

regex = r"[A-Z]"
if not re.search(regex, unos):
    print("Lozinka mora sadrzavati velika slova!")
    
regex = r"\d"
if not re.search(regex, unos):
    print("Lozinka mora sadrzavati broj!")

regex = r"\W"
if not re.search(regex, unos):
    print("Lozinka mora sadrzavati specijalni znak!")

regex = r".{8,}"
if not re.search(regex, unos):
    print("Lozinka mora sadrzavati barem osam znakova!")



