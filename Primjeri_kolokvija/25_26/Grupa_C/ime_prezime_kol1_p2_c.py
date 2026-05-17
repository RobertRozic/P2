'''
Grupa C
U datoteci products.py nalazi se lista od 8 proizvoda iz pekare. Svaki proizvod je tuple oblika:
	(sifra_proizvoda, naziv_proizvoda, cijena)

Učitavanje podataka
    Učitaj listu proizvoda iz datoteke products.py.

Pravila za šifru proizvoda
    Šifra proizvoda mora imati točno 4 znamenke, a prva znamenka mora biti 1 (npr. 1234, 1567).
    Provjerava se regularnim izrazom.

Simulacija narudžbi
    Za svaku narudžbu:
        Prikaži korisniku listu svih proizvoda sa šiframa i cijenama.
	Korisnik unosi šifru proizvoda koji želi naručiti.
	Unos šifre provjeri pomoću regexa. Ako unos nije valjan, narudžba se ne prihvaća i korisnik ponavlja unos.
	Nakon svake uspješne narudžbe, spremi naručeni proizvod i cijenu.
    Narudzbe se prekidaju unosom šifre 0000.

Spremanje narudžbi
    Svaku narudžbu spremi kao tuple:
	(sifra_proizvoda, naziv_proizvoda, cijena)

Analiza i izvještaj
    Na kraju ispiši:
        Ukupnu vrijednost svih narudžbi.
        Koji je proizvod najviše puta naručen.

Rezultate narudžbi spremi u tekstualnu datoteku narudzbe.txt u sljedećem formatu.
	Ukupno narudžbi: 5
	Ukupna vrijednost: 5.60 KM
	Najčešće naručen proizvod: Kifla
'''

from products import products

print(products)
