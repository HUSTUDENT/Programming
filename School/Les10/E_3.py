y = []
h = ""
def code(invoerstring):
    for x in invoerstring:
        nummer = ord(x)
        nummers = nummer + 3
        code = chr(nummers)
        y.append(code)
    print(h.join(y))

code("De appel valt niet ver van de boom, maar de boom valt ver van de appel")