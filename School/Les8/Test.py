aantalkluizen = 12
vrijekluizen = []
bezettekluizen = []
bezet=0
save = []
with open("kluizen.txt", "r+") as file:
    haha = file.readlines()
    print(haha)
    hahasplit = str(haha).split(",")
    hahasplit = str(hahasplit).split(";")
    print(hahasplit)
    for kluizen in range(1, aantalkluizen + 1):
        try:
            if hahasplit.count(kluizen)>0:
                print("Vol")
        except IndexError:
            None
    file.close()
    print(bezettekluizen)