cijferICOR = 8
cijferPROG = 10
cijferCSN = 8
bold = "\033[1m"
unbold = "\033[0;0m"
listcijfer = [cijferCSN, cijferICOR, cijferPROG]
gemiddelde = round(sum(listcijfer)/len(listcijfer), 2)
print(gemiddelde)
beloning = cijferPROG*30 + cijferICOR*30 + cijferCSN*30
print(beloning)
overzicht = "Mijn cijfers (gemiddeld een " + bold + str(gemiddelde) + unbold + ") leveren een beloning van " + bold + "€ " + str(beloning) + unbold + " op!"
print(overzicht)