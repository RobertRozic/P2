'''
Grupa A
U datoteci clubs.py nalazi se lista od 10 nogometnih klubova iz SHNL lige.
Svaki klub predstavljen je kao tuple oblika: (naziv_kluba, stadion).

Učitavanje podataka:
    Učitaj listu klubova iz datoteke clubs.py.

Formiranje parova:
    Nasumično formiraj parove klubova za odigravanje jednog kola (svaki klub igra jednu utakmicu).
    Za svaki par nasumično odredi koji je klub domaćin, a koji gost, te na kojem stadionu se igra utakmica (stadion domaćina).

Simulacija utakmica:
    Za svaku utakmicu nasumično generiraj broj golova za domaći i gostujući klub (npr. od 0 do 5).
    Sve utakmice spremati u listu riječnika oblika:
    {
        "domacin": "Dinamo Zagreb",
        "stadion": "Stadion Maksimir",
        "gost": "Hajduk Split",
        "golovi_domacin": 2,
        "golovi_gost": 1
    }

    Rezultate utakmice spremi novi array string-ova u formatu:
    NazivDomacina - NazivGosta, golovi_domacin:golovi_gost
    (npr. Dinamo - Hajduk, 1:1).

Analiza rezultata:
    Pomoću regularnih izraza (regex) provjeri u listi stringova i ispiši:
        U koliko utakmica je domaćin postigao barem jedan gol.
        U koliko utakmica je gost postigao barem jedan gol.

Zapis rezultata:
    Sve rezultate utakmica (stringove) ispiši na ekran i upiši u tekstualnu datoteku rezultati_kola.txt.
'''
