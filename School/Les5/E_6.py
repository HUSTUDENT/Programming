klinkers = ["a", "o", "u", "i", "e"]
s = "Guido van Rossum heeft programmeertaal Python bedacht."
lengte = len(s)
for x in range(0,lengte):
   if s[x] in klinkers:
       print(s[x])