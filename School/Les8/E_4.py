studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gemiddeldeperstudent = []
    for studentencijfer in studentencijfers:
        gemiddeldeperstudent.append(round(sum(studentencijfer)/len(studentencijfer),2))
    return gemiddeldeperstudent

def gemiddelde_van_alle_studenten(studentencijfers):
    return round(sum(gemiddelde_per_student(studentencijfers))/len(gemiddelde_per_student(studentencijfers)),2)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
