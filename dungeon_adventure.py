import random

def main():
    def setup_player():

        name = input("Enter your name: ")
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }

        return player


    def create_treasures():
        
        treasures = {
        "gold coin": random.randint(3, 12),
        "ruby": random.randint(3, 12),
        "ancient scroll": random.randint(3, 12),
        "emerald": random.randint(3, 12),
        "silver ring": random.randint(3, 12)
    }
    
        return treasures

    def display_options(room_number):

        print(f"You are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
        
            player["inventory"].append(item)
        
            print(f"You found a {item} worth {treasures[item]} points!")
    
        else:
        # Trap: lose health
            player["health"] -= 2
        
        # Print warning
            print("Oh no! You triggered a trap and lost 2 health!")

        return player

    def check_status(player):
    
         print(f"Health: {player['health']}")

         if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))

         else:
            print("Inventory: You have no items yet.")

    def end_game(player, treasures):
        total_score = 0
        for item in player["inventory"]:
            total_score += treasures.get(item, 0)

    
        print(f"Final Health: {player['health']}")

        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
             print("Inventory: You have no items.")

        print(f"Total Score: {total_score}")
        print("Game Over! Thanks for playing.")

    def run_game_loop(player, treasures):
        
        for room_number in range(1, 6):
            while True:
                display_options(room_number)
                choice = input("Enter your choice (1-4): ").strip()

                if choice == "1":
                    search_room(player, treasures)

                # End game early if health drops below 1
                    if player["health"] < 1:
                        print("Your health has dropped to 0.")
                        end_game(player, treasures)
                        return

                elif choice == "2":
                    print(f"You move on from room {room_number}.\n")
                    break

                elif choice == "3":
                    show_player_status(player)

                elif choice == "4":
                    print("You chose to quit the game.")
                    end_game(player, treasures)
                    return

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # After all 5 rooms are completed
        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
