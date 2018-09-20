prijs = 4356
try:
    personen = int(input("Met hoeveel personen ga je? "))
    if personen <0:
        print("Negatieve getallen zijn niet toegestaan!")
    else:
        print("De prijs voor " + str(personen) + " personen is " + str(round((prijs/personen),2)) + " euro per persoon")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except:
    print("Onjuiste invoer!")