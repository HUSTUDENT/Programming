invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
InvoerList = invoer.split("-")
IntInvoer = []
for Invoer in InvoerList:
    IntInvoer.append(int(Invoer))
IntInvoer.sort()
print("Gesorteerde list van ints: " + str(IntInvoer))
print("Grootste getal: " + str(max(IntInvoer)) + " en Kleinste getal: " + str(min(IntInvoer)))
print("Aantal getallen: " + str(len(IntInvoer)) + " en Som van de getallen: " + str(sum(IntInvoer)))
print("Gemiddelde: " + str(sum(IntInvoer)/len(IntInvoer)))
