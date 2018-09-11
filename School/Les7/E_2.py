namen = []
nummers = []
with open("kaartnummers.txt", "r") as file:
    files = file.readlines()
    for line in files:
        words = line.split(",")
        words[1] = words[1].strip("\n")
        namen.append(words[1])
        nummers.append(words[0])
    print(namen[0] + " heeft kaartnummer: " + nummers[0] + "\n" + namen[1] + " heeft kaartnummer: " + nummers[1] + "\n" +namen[2] + " heeft kaartnummer: " + nummers[2] + "\n" +namen[3] + " heeft kaartnummer: " + nummers[3] + "\n" +namen[4] + " heeft kaartnummer: " + nummers[4] + "\n" +namen[5] + " heeft kaartnummer: " + nummers[5])
