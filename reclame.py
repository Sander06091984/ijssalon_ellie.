from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    nieuwe_prijs_afgerond = round(nieuwe_prijs, 2)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs_afgerond} euro."
print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
print(inkomsten_totaal(inkomsten, btw))


mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    avg = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {avg} euro."

invoer_lijst = [10,5,3,2,1,2,9]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer