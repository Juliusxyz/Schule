target_number = 33
print("Errate die Zahl zwischen 1 und 100!")

while True:
    try:
        guess = int(input("Dein Tipp: "))
        if guess < target_number:
            print("Zu niedrig!")
        elif guess > target_number:
            print("Zu hoch!")
        else:
            print("Herzlichen Glückwunsch! Du hast die Zahl erraten.")
            break
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")