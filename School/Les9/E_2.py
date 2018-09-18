while 1 == 1:
    woord = input("Geef een string van vier letters: ")
    if len(woord) != 4:
        print(woord + " heeft " + str(len(woord)) + " letters")
    else:
        print("Inlezen van correcte string: " + woord + " is geslaagd")
        break