'''
Napisati regex za validaciju unešene lozinke.

Lozinka mora sadržavati:
Veliko slovo
Broj
Specijalni znak
Biti duža od 8 znakova
'''
import re

lozinka = input("Unesite lozinku:")

valid = True

regex = "[A-Z]"
if not re.search(regex, lozinka):
    valid = False
    print('Lozinka mora sadrzavati barem jedno veliko slovo!')

regex = "\d"
if not re.search(regex, lozinka):
    valid = False
    print('Lozinka mora sadrzavati barem jedan broj!')

regex = "\W"
if not re.search(regex, lozinka):
    valid = False
    print('Lozinka mora sadrzavati barem jedan specijalni znak!')

regex = '.{8}'
if not re.search(regex, lozinka):
    valid = False
    print('Lozinka mora imati barem 8 znakova!')

if valid:
    print('Lozinka je sigurna!')

