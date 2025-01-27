import random # Für die Zufallsauswahl der Kugeln
import time  # Für die Wartezeit der KI

def main():
    class Player:
        def __init__(self, name):
            self.name = name
            self.alive = True

        def take_turn(self, chamber, is_ai=False):
            if self.alive:
                if is_ai:
                    print(f"\n{self.name}'s turn. The AI is thinking...")
                    time.sleep(2)  # KI wartet 2 Sekunden
                    print(f"{self.name} pulls the trigger...")
                else:
                    input(f"{self.name}, press Enter to pull the trigger...")

                if chamber == 1:
                    self.alive = False
                    print(f"\n💥 {self.name} has been shot! 💀")
                else:
                    print(f"\n🎉 {self.name} is safe!")

    def play_game(players, num_bullets):
        # Initialize the revolver chambers
        chambers = [0] * 6
        bullet_positions = random.sample(range(6), num_bullets)
        for pos in bullet_positions:
            chambers[pos] = 1

        chamber_index = 0

        while len([p for p in players if p.alive]) > 1:
            for player in players:
                if player.alive:
                    chamber = chambers[chamber_index]
                    player.take_turn(chamber, is_ai=(player.name == "AI"))

                    # Rotate the chamber
                    chamber_index = (chamber_index + 1) % 6

                    if not player.alive:
                        break

        winner = next(p for p in players if p.alive)
        print(f"\n🎉 {winner.name} wins! Congratulations!")

    if __name__ == "__main__":
        try:
            print("Welcome to Russian Roulette!")
            mode = input("Choose mode: Singleplayer (1) or Multiplayer (2): ").strip()

            if mode == "1":  # Singleplayer
                player_name = input("Enter your name: ")
                player = Player(player_name)
                ai = Player("AI")
                players = [player, ai]

                num_bullets = int(input("Enter the number of bullets (1-5): "))
                if 1 <= num_bullets <= 5:
                    play_game(players, num_bullets)
                else:
                    print("Invalid number of bullets. Please enter a number between 1 and 5.")

            elif mode == "2":  # Multiplayer
                num_players = int(input("Enter the number of players (2-4): "))
                if 2 <= num_players <= 4:
                    players = []
                    for i in range(num_players):
                        name = input(f"Enter name for Player {i + 1}: ")
                        players.append(Player(name))

                    num_bullets = int(input("Enter the number of bullets (1-5): "))
                    if 1 <= num_bullets <= 5:
                        play_game(players, num_bullets)
                    else:
                        print("Invalid number of bullets. Please enter a number between 1 and 5.")
                else:
                    print("Invalid number of players. Please enter a number between 2 and 4.")
            else:
                print("Invalid mode. Please choose 1 or 2.")

        except ValueError:
            print("Please enter a valid number.")

main()
