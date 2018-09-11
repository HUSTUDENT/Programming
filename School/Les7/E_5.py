def gemiddelde(zin):
    woorden = zin.split(" ")
    lengte = len(woorden)
    totalelengte = 0
    for woord in woorden:
        woordlengte = len(woord)
        totalelengte = totalelengte + int(woordlengte)
    print("De gemiddelde lengte van de woorden in je zin zijn: " + str(totalelengte/lengte) + " letters per woord")
gemiddelde(zin = input("Type je zin: "))
