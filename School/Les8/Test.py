aantalkluizen = 12
vrijekluizen = []
bezettekluizen = []
with open("kluizen.txt","r+") as file:
    for kluizen in range(1,aantalkluizen+1):
        try:
            bezet = file.readlines(kluizen)[0][0]
        except IndexError:
            None
        if str(kluizen) == bezet:
            bezettekluizen.append(kluizen)
        else:
            vrijekluizen.append(kluizen)
    file.close()
print(vrijekluizen)
print(bezettekluizen)
