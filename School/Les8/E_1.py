def seizoen(maand):
    Lente = (3,4,5)
    Zomer = (6,7,8)
    Herfst = (9,10,11)
    Winter = (12,1,2)
    if maand in Lente:
        return "Lente"
    if maand in Zomer:
        return "Zomer"
    if maand in Herfst:
        return "Herfst"
    if maand in Winter:
        return "Winter"

print(seizoen(6))