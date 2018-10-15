aantalkluizen = 12
vrijekluizen = []
bezettekluizen = []
bezet=0
save = []
with open("kluizen.txt", "r+") as file:
    for kluizen in range(1, aantalkluizen + 1):
        try:
            bezet = file.readlines(kluizen)[0]
            bezet = bezet.split(";")
            bezettekluizen.append(int(bezet[0]))
        except IndexError:
            None
        if kluizen not in bezettekluizen:
            vrijekluizen.append(kluizen)
    file.close()
print(vrijekluizen)
print(bezettekluizen)
def toon_aantal_kluizen_vrij():
    return len(vrijekluizen)
def nieuwe_kluis():
    if len(vrijekluizen)>0:
        code = input("Vul je gewenste code in: ")
        if len(code)>=4:
            with open("kluizen.txt", "a") as file:
                file.write(str(vrijekluizen[0]) + ";" + str(code) + "\n")
                file.close()
                kluis = vrijekluizen[0]
                bezettekluizen.append(kluis)
                vrijekluizen.remove(kluis)
            return "Je krijgt kluis: " + str(kluis)
        else:
            return "Geen geldige code, hij moet minimaal 4 tekens lang zijn"
    else:
        return "Alle kluizen zijn vol"
def kluis_openen():
    kluischeck = input("Wat is je kluisnummer: ")
    if int(kluischeck) in vrijekluizen:
        return "Die kluis is niet bezet"
    codecheck = input("Wat is je code: ")
    if int(len(codecheck))<4:
        return "Dat is geen geldige code"
    with open("kluizen.txt", "r") as file:
        for tekst in file.readlines():
            if tekst[0] == kluischeck:
                tekstcheck = (str(tekst).split(";"))
                codecontrole = tekstcheck[1].replace("\n","")
                if codecontrole == codecheck:
                    vrijekluizen.append(kluischeck)
                    bezettekluizen.remove(kluischeck)
                    return "Je kluis is open"
                file.close()
                return "Foute code"
    return "Dit kluisnummer bestaat niet"
def kluis_teruggeven():
    kluischeck = input("Wat is je kluisnummer: ")
    if int(kluischeck) in vrijekluizen:
        return "Die kluis is niet bezet"
    codecheck = input("Wat is je code: ")
    if int(len(codecheck))<4:
        return "Dat is geen geldige code"
    with open("kluizen.txt", "r") as file:
        for tekst in file.readlines():
            if tekst[0] == kluischeck:
                tekstcheck = (str(tekst).split(";"))
                codecontrole = tekstcheck[1].replace("\n","")
                if codecontrole == codecheck:
                    save=[]
                    with open("kluizen.txt", "r") as file:
                        for te in file.readlines():
                            if te != tekst:
                                save.append(te)
                            with open("kluizen.txt", "w") as file:
                                for a in save:
                                    file.write(a)
                            file.close()
                    file.close()
                    return "Je kluis is nu gereset"
                return "Foute code"
            return "Dit kluisnummmer bestaat niet"
while True:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn" + "\n" + "2: Ik wil een nieuwe kluis" + "\n" + "3: Ik wil even iets uit mijn kluis halen" + "\n" + "4: Ik geef mijn kluis terug" + "\n" + "5: Ik wil stoppen")
    keuze = input("Ik kies optie: ")
    try:
        if int(keuze) > 5 or int(keuze) < 0:
            print("Kies een van de vijf opties")
        else:
            if keuze == "5":
                break
            elif keuze == "4":
                print(kluis_teruggeven())
            elif keuze == "3":
                print(kluis_openen())
            elif keuze == "2":
                print(nieuwe_kluis())
            elif keuze == "1":
                print("Er zijn nog "+ str(toon_aantal_kluizen_vrij()) + " kluizen vrij")
    except ValueError:
        print("Je moet wel iets invullen")