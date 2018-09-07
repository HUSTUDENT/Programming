leeftijd = int(input("Geef je leeftijd: "))
paspoort = input("Nederlands paspoort: ")
while paspoort not in ("ja", "Ja", "JA", "nee", "Nee", "NEE"):
    print("U kunt alleen maar antwoorden met een ja of nee")
    paspoort = input("Nederlands paspoort: ")
if leeftijd >= 18 and (paspoort == "Ja" or paspoort == "JA" or paspoort == "ja"):
    print("Gefeliciteerd, u mag stemmen")
else:
    print("Helaas, u mag niet stemmen")