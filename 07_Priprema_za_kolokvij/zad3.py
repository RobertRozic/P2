import re

lozinka = input("Unesi lozinku:")

# Provjera velikog slova
reg = "[A-Z]"
if re.search(reg, lozinka):
    print("Ima veliko slovo!")
else:
    print("Lozinka nema veliko slovo!")

# Provjera broja
reg = "\d"
if re.search(reg, lozinka):
    print("Ima broj!")
else:
    print("Lozinka nema broj!")

reg = "\W"
if re.search(reg, lozinka):
    print("Ima specijalni znak!")
else:
    print("Lozinka nema specijalni znak!")

reg = ".{8,}"
if re.search(reg, lozinka):
    print("Lozinka dulja od 8 znakova")
else:
    print("Lozinka prekratka!")
    


