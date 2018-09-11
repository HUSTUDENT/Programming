nummers = []
with open("kaartnummers.txt", "r") as file:
    lengte = len(file.readlines())
    files = file.readlines()
    for line in files:
        words = line.split(",")
        nummers.append(words[0])
    print(nummers)