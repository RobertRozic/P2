# 1. Učitaj datoteku studenti.txt u read modu te iz nje dohvati popis studenata.
# Zanemari prvu liniju u kojoj se nalazi zaglavlje
# Od podataka napravi listu uređenih parova ime,prezime

dat = open("studenti.txt", "r", encoding="utf-8")

# 2. Iteriranjem kroz listu uređenih parova n-torki koristeći svojstvo raspakiravanja,
# kreiraj listu rječnika sa ključevima ime i prezime.

# 3. Ponovnim iteriranjem kroz listu, svakom od studenata dodaj novo svojstvo (key) ocjena.
# Ocjena bi trebala imati nasumičnu vrijednost od 1 do 5 - integer
# U novi rječnik prebroji koliko studenata je dobilo koju ocjenu.

# 4. Od korisnika zatražiti unos imena od minimalno 3 znaka i prvim velikim slovom.
# Unos provjeravati pomoću regexa. Tražitu unos sve dok se ne unese ispravna vrijednost.
# Iz rječnika studenata pronaći sve osobe tog imena i ispisati njihovo ime, prezime i ocjenu.
# Ukoliko osoba s tim imenom ne postoji u rjecniku, ispisati da osoba ne postoji.

