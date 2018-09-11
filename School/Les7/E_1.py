def convert(Celsius):
    Fahrenheit = Celsius * 1.8 + 32
    return Fahrenheit

def table():
    print("  F    C")
    C = -30
    width = 5
    for c in range(0,8):
        print(f'{int(convert(C)):4d} {int(C):4d}')
        C = C + 10

table()
