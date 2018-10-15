aantalkluizen = 12
vrijekluizen = []
bezettekluizen = []
bezet=0
save = []
with open("kluizen.txt", "r+") as file:
    for kluizen in range(1, aantalkluizen + 1):
         bezet = file.readlines(kluizen)
         print(bezet)