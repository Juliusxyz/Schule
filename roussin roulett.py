import random
import os

chambers = input("Gebe eine Nummer der Kammern ein")

if chambers.isdigit():
    if not chambers:
        chambers = 5

elif not chambers.isdigit():
    quit("Keine richtiege nummer")

fatal_bullet = random.randint(1, int(chambers))

for x in range(1, int(chambers) + 1):
    input("Drücke Enter zum schießen! ")
    if x == fatal_bullet:
        print("Du bist tot!")
        print("Game Over")
        start_again = input("Möchtest du nochmal spielen? (y/n): ")
        if start_again and start_again.lower()[0] == "y":
            continue
        else:
            break
    print("Du hast überlebt!")

    


