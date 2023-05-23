tekst = "In the 1980s, the more complicated regexes arose in Perl, which originally derived from a regex library written by Henry Spencer (1986), who later wrote an implementation of Advanced Regular Expressions for Tcl.[13] The Tcl library is a hybrid NFA/DFA implementation with improved performance characteristics. Software projects that have adopted Spencer's Tcl regular expression implementation include PostgreSQL.[14] Perl later expanded on Spencer's original library to add many new features.[15] Part of the effort in the design of Raku (formerly named Perl 6) is to improve Perl's regex integration, and to increase their scope and capabilities to allow the definition of parsing expression grammars.[16] The result is a mini-language called Raku rules, which are used to define Raku grammar as well as provide a tool to programmers in the language. These rules maintain existing features of Perl 5.x regexes, but also allow BNF-style definition of a recursive descent parser via sub-rules."
tekst = tekst.lower()

brojac = {}

for slovo in tekst:
    brojac[slovo]= brojac.get(slovo, 0) + 1

print(brojac)

brojac = {key: brojac[key]
          for key in sorted(brojac.keys())}

print(brojac.keys())

kljucevi = brojac.keys()

print(kljucevi)

if "x" in kljucevi or "y" in kljucevi or "w" in kljucevi:
    print("Engleski tekst")

'''
parovi = []
for el in brojac:
    par = el, brojac[el]
    parovi.append(par)
print(parovi)
'''
elementi = brojac.items()
print(elementi)

for slovo, ponavljanja in elementi:
    print("Slovo", slovo, "se pojavljuje", ponavljanja, "puta.")





