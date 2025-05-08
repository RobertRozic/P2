# Zadatak
# Podatke iz datoteke rezultati.csv
# učitati kao listu ntorki oblika (ime, prezime, bodovi).
# Iterirati kroz sve studente i ispisati
# samo one koji su položili ispit (br. bodova veci od 49)
import csv

csv_file_path = 'rezultati_25.csv'

with open(csv_file_path, 'r', encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

ntorke = []
for row in data_list:
    ntorka = row[0], row[1], row[2] # poredak
    ntorke.append(ntorka)

print(ntorke)

# tuple way
for ime, prezime, bodovi in ntorke:
    if int(bodovi) > 49:
        print("Student", ime, prezime, "je polozio ispit!")
    




