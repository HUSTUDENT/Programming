getal = 1
getallen = []
while getal != 0:
    getal = int(input("Geef een getal: "))
    getallen.append(getal)
print("Er zijn " + str(len(getallen)) + " getallen ingevoerd, de som is: " + str(sum(getallen)))