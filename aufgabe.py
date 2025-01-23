import math

zahl = input("Gebe eine Zahl ein: ")
if zahl.isdigit():
            zahl = int(zahl)
            wurzel = math.sqrt(zahl)
            print(f"Die Quadratwurzel von {zahl} ist {wurzel}")
else:
            print("Bitte nur Zahlen eingeben.")