def standaartarief(afstandKM):
    if afstandKM > 50:
        prijs = round(15 + 0.6*afstandKM,2)
    else:
        if afstandKM > 0:
            prijs = round(0.8*afstandKM,2)
        else:
            prijs = 0
    return(prijs)

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs = standaartarief(afstandKM)
    if (leeftijd < 12 or leeftijd >= 65) and weekendrit == True:
        korting =  35
    else:
        if (leeftijd < 12 or leeftijd >= 65) and weekendrit == False:
            korting = 30
        else:
            if weekendrit == True:
                korting = 40
            else:
                korting = 0
    return round(standaardprijs/100*(100-korting),2)

print(standaartarief(20))
print(ritprijs(65,False,20))

