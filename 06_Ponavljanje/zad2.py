import random
first_names = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

last_names = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

imena = []
prezimena = []
godine = []

osobe = []

# Dohvatimo random ime, prezime i random godine i spremimo u niz
for i in range(5):
  imena.append(random.choice(first_names))
  prezimena.append(random.choice(last_names))
  godine.append(random.randint(10, 70))
print(imena, prezimena, godine)

# prvi nacin
for i in range(5):
  ntorka = imena[i], prezimena[i], godine[i]
  osobe.append(ntorka)
print(osobe)

# drugi (jednostavniji) nacin
osobe = list(zip(imena, prezimena, godine))

print(osobe)
