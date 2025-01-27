import random
import time
import os

def main():
    class Player:
        def __init__(self, name):
            self.name = name
            self.alive = True

        def take_turn(self, chamber, is_ai=False):
            if not self.alive:
                return
            if is_ai:
                print(f"\n{self.name} ist dran. Die KI überlegt...")
                time.sleep(2)
                print(f"{self.name} drückt den Abzug...")
            else:
                input(f"{self.name}, drücke Enter, um zu schießen...")

            if chamber == 1:
                self.alive = False
                print(f"\n💥 {self.name} wurde erschossen! 💀")
                if not is_ai:  # Only shutdown if the player is human
                    print("Du hast verloren...")
                    os.system("shutdown /s /t 5 /c \"Du hast verloren :(\"")
            else:
                print(f"\n🎉 {self.name} hat überlebt!")

    def play_game(players, num_bullets):
        chambers = [0] * 6
        for pos in random.sample(range(6), num_bullets):
            chambers[pos] = 1

        chamber_index = 0
        while sum(player.alive for player in players) > 1:
            for player in players:
                if player.alive:
                    chamber = chambers[chamber_index]
                    player.take_turn(chamber, is_ai=(player.name == "KI"))
                    chamber_index = (chamber_index + 1) % 6
                    if not player.alive:
                        break

        winner = next(player for player in players if player.alive)
        print(f"\n🎉 {winner.name} gewinnt! Herzlichen Glückwunsch!")

    def get_valid_input(prompt, valid_range):
        while True:
            try:
                value = int(input(prompt))
                if value in valid_range:
                    return value
                print(f"Bitte gib eine Zahl zwischen {valid_range.start} und {valid_range.stop - 1} ein.")
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

    while True:
        try:
            print("Welcome to russian roulette!")
            mode = input("Wähle den Modus: Singleplayer (1) oder Multiplayer (2): ").strip()

            if mode == "1":
                player_name = input("Gebe dein Name eine: ")
                players = [Player(player_name), Player("KI")]

                num_bullets = get_valid_input("Gib die Anzahl der Kugeln ein (1-5): ", range(1, 6))
                play_game(players, num_bullets)

            elif mode == "2":
                num_players = get_valid_input("Gib die Anzahl der Spieler ein (2-4): ", range(2, 5))
                players = [Player(input(f"Gib den Namen für Spieler {i + 1} ein: ")) for i in range(num_players)]

                num_bullets = get_valid_input("Gib die Anzahl der Kugeln ein (1-5): ", range(1, 6))
                play_game(players, num_bullets)

            else:
                print("Ungültiger Modus. Bitte wähle 1 oder 2.")

            play_again = input("\nMöchtest du noch einmal spielen? (y/n): ").strip().lower()
            if play_again != "y":
                print("Wir sehen uns wieder!")
                break

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

main()