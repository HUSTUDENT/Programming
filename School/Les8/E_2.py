List = eval(input("Geef lijst met minimaal 10 strings: "))
VierList = []
for x in range(0,len(List)):
    if len(List[x]) == 4:
        VierList.append(List[x])
print("De nieuw-gemaakte lijst met alle vier-letter strings is:" + str(VierList))