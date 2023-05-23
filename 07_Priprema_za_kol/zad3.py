# Napisati regex za validaciju unešene lozinke.
#Lozinka mora sadržavati:
#Veliko slovo
#Broj
#Specijalni znak
#Biti duža od 8 znakova
import re

lozinka = input("Unesi lozinku: ")

# Pravilo 1. - Duljina
duljina = len(lozinka)
if duljina < 8:
  print("Lozinka mora sadrzavati minimalno 8 znakova.")

# Pravilo 2. - Veliko slovo
regex1 = '[A-Z]'
veliko = re.findall(regex1, lozinka)
if not veliko:
  print("Lozinka mora sadrzavati barem jedno veliko slovo.")

# Pravilo 3. - broj
regex2 = '[0-9]' # '\d'
broj = re.findall(regex2, lozinka)
if not broj:
  print("Lozinka mora sadrzavati barem jedan broj.")

# Pravilo 4.
regex3 = '[^a-zA-Z0-9_]' # '\W'
specijalni = re.findall(regex3, lozinka)
if not specijalni:
  print("Lozinka mora sadrzavati barem specijalni znak.")

if duljina >= 8 and veliko and broj and specijalni:
  print("Lozinka je sigurna!")
