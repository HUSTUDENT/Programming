cijfers = {
   "Student1": 5,
   "Student2": 10,
   "Student3": 9,
   "Student4": 6,
   "Student5": 8,
   "Student6": 10,
   "Student7": 9,
   "Student8": 3,
   "Student9": 9.5
}
for x,y in cijfers.items():
    if y >= 8   :
        print(x + " heeft een " + str(y))