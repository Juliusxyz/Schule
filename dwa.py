import cmath

a = float(input("Gebe die Variable a ein: "))
b = float(input("Gebe die Variable b ein: "))
c = float(input("Gebe die Variable c ein: "))

if a != 0:
    dings = b**2 - 4*a*c
    loesung1 = (-b + cmath.sqrt(dings)) / (2*a)
    loesung2 = (-b - cmath.sqrt(dings)) / (2*a)
    print(f"Die Lösungen der quadratischen Gleichung sind: {loesung1} und {loesung2}")
else:
    print("Dies ist keine quadratische Gleichung, da a = 0 ist.")