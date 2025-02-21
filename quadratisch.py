while True:
    while True:
        zahl1 = input("Gebe die erste Zahl ein: ")
        if zahl1.isdigit():
            zahl1 = int(zahl1)
            break
        else:
            print("Bitte nur Zahlen eingeben.")

    while True:
        zahl2 = input("Gebe die zweite Zahl ein: ")
        if zahl2.isdigit():
            zahl2 = int(zahl2)
            break
        else:
            print("Bitte nur Zahlen eingeben.")

    operation = input("Möchtest du addieren (+), subtrahieren (-), multiplizieren (*) oder dividieren (/)? ")

    if operation == '+':
        ergebnis = zahl1 + zahl2
    elif operation == '-':
        ergebnis = zahl1 - zahl2
    elif operation == '*':
        ergebnis = zahl1 * zahl2
    elif operation == '/':
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            ergebnis = "Fehler: Division durch Null"
    else:
        ergebnis = "Ungültige Operation"

    print(f"Das Ergebnis ist: {ergebnis}")

    wiederholen = input("Möchtest du das Programm beenden? (y/n): ").lower()
    if wiederholen == 'y':
        break