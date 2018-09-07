def kwadraten_som(grondgetallen):
    goedegetallen = []
    for grondgetal in grondgetallen:
        if grondgetal>=0:
            goedegetallen.append(int(grondgetal**2))
    return sum(goedegetallen)

getallen = [1,2,3,4,5,6,7,8,9,10]
print(kwadraten_som(getallen))
dd