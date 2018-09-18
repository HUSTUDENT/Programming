dict = {}
def ticker(filename):
    with open("bedrijven.txt","r+") as file:
        for x in file.readlines():
            y = x.split(":")
            if y[0] == filename:
                dict[y[0]] = y[1]
    file.close()
    print(dict)

ticker("YAHOO")
