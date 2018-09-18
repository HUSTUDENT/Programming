dict={}
def namen():
    while 1 == 1:
        z = input("Volgende naam: ")
        if z == "":
            break
        if dict.get(z) == None:
            dict[z] = 1
        else:
            aantal = dict.get(z)
            dict[z] = aantal + 1
    for naam in dict:
        aantalnaam = str(dict.get(naam))
        if aantalnaam == "1":
            print("Er is " + aantalnaam + " student met de naam " + naam)
        else:
            print("Er zijn " + aantalnaam + " studenten met de naam " + naam)

namen()