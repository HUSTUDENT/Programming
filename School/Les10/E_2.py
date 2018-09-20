from random import *
def monopolyworp():
    random1 = randint(1,6)
    random2 = randint(1,6)
    if random1 == random2:
        print(str(random1) + " + " + str(random2) + " = " + str(random1 + random2) + " (dubbel)")
        random3 = randint(1,6)
        random4 = randint(1,6)
        if random3 == random4:
            print(str(random3) + " + " + str(random4) + " = " + str(random3 + random4) + " (dubbel)")
            random5 = randint(1,6)
            random6 = randint(1,6)
            if random5 == random6:
                print(str(random5) + " + " + str(random6) + " = (direct naar de gevangenis)")
            else:
                print(str(random5) + " + " + str(random6) + " = " + str(random5 + random6))
        else:
            print(str(random3) + " + " + str(random4) + " = " + str(random3 + random4))
    else:
        print(str(random1) + " + " + str(random2) + " = " + str(random1 + random2))

monopolyworp()
