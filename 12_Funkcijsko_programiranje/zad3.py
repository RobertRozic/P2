# Kao što funkciju možemo poslati kao argument,
# također ona može biti 
# povratna vrijednost neke funkcije

def vanjska():
    def unutarnja():
        print("Ja sam funkcija unutarnja()!")
    return unutarnja

ime_funkcije = vanjska()
ime_funkcije()

