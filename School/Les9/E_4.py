dict = {}
def ticker(filename):
    with open(filename, "r+") as file:
        for x in file.readlines():
            y = x.split(":")
            normal = y[1].replace("\n", "")
            dict[y[0]] = normal
    file.close()
    return dict

bedrijfsnaam = input("Enter Company name: ")
print("Ticker symbol: " + ticker("bedrijven.txt").get(bedrijfsnaam))
tickernaam = input("Enter Ticker symbol: ")
for z in ticker("bedrijven.txt"):
    if ticker("bedrijven.txt").get(z) == tickernaam:
        print("Company name: " + z)