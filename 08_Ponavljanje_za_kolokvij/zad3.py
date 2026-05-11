'''
Napisati regex za validaciju unešene lozinke.

Lozinka mora sadržavati:
Veliko slovo
Broj
Specijalni znak
Biti duža od 8 znakova
'''
import re

while True:
    greske = 0
    unos = input("Unesi lozinku:")

    regex = '[A-Z]'
    if not re.search(regex, unos):
        print("Lozinka mora sadrzavati veliko slovo!")
        greske += 1

    regex = '\d'
    if not re.search(regex, unos):
        print("Lozinka mora sadrzavati broj!")
        greske += 1

    regex = '\W'
    if not re.search(regex, unos):
        print("Lozinka mora sadrzavati specijalni znak!")
        greske += 1

    regex = '.{8,}'
    if not re.search(regex, unos):
        print("Lozinka mora imati 8 ili vise znakova!")
        greske += 1

    if greske == 0:
        break
