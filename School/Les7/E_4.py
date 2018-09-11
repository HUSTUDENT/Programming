import datetime
with open("hardlopers.txt", "a+") as file:
    naam = input("Naam van de hardloper: ")
    vandaag = datetime.datetime.today()
    info = vandaag.strftime("%a %d %b %Y" + "," +" %H" + ":" + "%M" + ":" + "%S" + ", ")
    print(info + naam)
    file.writelines(info + naam + "\n")
    file.close()