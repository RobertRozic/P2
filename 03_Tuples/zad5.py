from csv import reader
# read csv file as a list of lists

# open file in read mode
with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    studenti = list(map(tuple, csv_reader))
    # display all rows of csv
    #print(list_of_tuples)

print("Polozili su:")
for ime, prezime, bodovi in studenti:
    if int(bodovi) > 49:
        print(ime, prezime)

ocjene = {
    "izvrstan": 0,
    "vrlo dobar": 0,
    "dobar": 0,
    "dovoljan": 0,
    "nedovoljan": 0
}

#
#
