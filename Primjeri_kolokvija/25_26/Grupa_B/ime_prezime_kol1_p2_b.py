'''
Grupa B
U datoteci questions.py nalazi se lista od 10 pitanja za kviz. Svako pitanje je rječnik oblika:

{
    "pitanje": "Koji je glavni grad Hrvatske?",
    "a": "Zagreb",
    "b": "Split",
    "c": "Rijeka"
    "tocan": "a"
}

Učitavanje podataka
    Učitaj listu pitanja iz datoteke questions.py.

Postavljanje pitanja korisniku
    Za svako pitanje:
        Prikaži tekst pitanja i ponuđene odgovore (a, b, c).
        Zatraži unos korisnika (a, b ili c).
        Unos provjeri pomoću regularnog izraza. Ako unos nije valjan, tretiraj ga kao pogrešan odgovor.

Spremanje rezultata
    Za svaki odgovor u array odgovori spremi tuple oblika:
	(pitanje, korisnikov_odgovor, tocan_odgovor, tocno/netocno)
    Gdje je tocno True ako je korisnikov odgovor točan, inače False.

Analiza i bodovanje
    Svaki točan odgovor nosi 1 bod.
    Na kraju kviza:
        Ispiši broj osvojenih bodova i postotak uspješnosti.
        Ispiši listu svih pitanja i za svako prikaži je li odgovor bio točan ili ne.

Rezultate kviza spremi u tekstualnu datoteku rezultati_kviza.txt u sljedećem formatu:
	Ukupno bodova: 7/10
	Uspješnost: 70%
'''

from questions import questions

print(questions)
