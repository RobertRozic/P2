#Napisati program koji broji broj slova u tekstu koristeci rječnike.
#Ključevi rječnika su slova, a vrijednosti broj ponavljanja.
#Provjeriti pojavljuju li se u tekstu engleski znakovi (x, y, w) ili #brojevi.
#Iz rječnika dohvatiti uređene parove slova i broj ponavljanja te #iterirati kroz for petlju i ispisati. 


tekst = "A regular expression (shortened as regex or regexp;sometimes referred to as rational expression) is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for find or find and replace operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory. The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language."

# Inicijaliziranje praznog rjecnika
slova = {}

# Prolazak kroz sva slova u tekstu
for slovo in tekst:
  # pretvaramo sva slova u mala
  slovo = slovo.lower()
  # na key slovo, dohvacamo staru vrijednost i uvecavamo je za 1
  # Ukoliko nema tog kljuca, default vrijednost je 0
  slova[slovo] = slova.get(slovo, 0) + 1

# Ispis
print(slova)

# Provjera ima li x, y, w
# for petljom
for slovo in tekst:
  if slovo in ['x', 'y', 'w']:
    print("Postoje x, y ili w")
    
# Rjecnici
# Prolazak kroz sva engleska slova for petljom i ispis
# koliko puta se pojavljuju
for eng in ['x','y','w']:
  print(eng, "se pojavljuje:", slova.get(eng, 0), "puta")

# Prolazak kroz sve znamenke od 0 do 10
# pretvaramo ih u string jer su nam kljucevi rjencika string
for n in range(10):
  print(n, "se pojavljuje:", slova.get(str(n), 0), "puta")

# Metoda 1
#parovi = []
#for key in slova:
#  parovi.append((key, slova[key]))

# ili
# pretvaranje rjecnika u niz ntorki (tuples)
parovi = slova.items()

# Raspakiramo parove u dvije varijable, slova i ponavljanja 
for slovo, ponavljanja in parovi:
  print(slovo, ponavljanja)

