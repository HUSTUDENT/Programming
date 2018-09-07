score = input("Geef je score: ")
if int(score) > 15:
    print("Gefeliciteerd!")
    print("Met een score van " + score + " ben je geslaagd!")
if int(score) <=15:
    print("Jammer....")
    print("Je hebt het helaas niet gehaald, je mist nog minimaal " + str(16-int(score)) + " punten")