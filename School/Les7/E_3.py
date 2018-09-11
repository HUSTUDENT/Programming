nummers = []
with open("kaartnummers.txt", "r") as file:
    files = file.readlines()
    lengte = str(len(files))
    for line in files:
        words = line.split(",")
        nummers.append(words[0])
    print("Deze file telt " + lengte + " regels" + "\n" + "Het grootste kaartnummer is: " + str(max(nummers)) + " en dat staat op regel " + str(nummers.index(max(nummers))+1))
    file.close()