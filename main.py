# Import necessary modules and classes
__author__ = "AndyVoyager"

from logic import Game, Symbols
from art import welcome, goodbye, rules, start, draw
from time import sleep

# Initialize the game symbols
symbols = Symbols()

# Display welcome message
print(welcome)

# Start the main loop for the game
while True:

    # Ask the player if they want to play or see the rules
    play_or_rules = input("Do you want to play or see the rules? (play/rules/exit) ").lower()

    # If the player chooses to see the rules
    if play_or_rules == "rules":
        print(rules)

    # If the player chooses to play
    elif play_or_rules == "play":
        print(start)

        # Initialize the game and create the game table
        game_manager = Game()
        game_manager.create_table()
        table = game_manager.table
        print(game_manager.show_table(inp_table=table))

        # Start the game loop
        play_game = True
        while play_game:
            # Check if the first player's choose is valid
            try:
                # Loop for the first player's turn
                while True:
                    user1 = input("User1/Crosses choose your position: ").lower()
                    # If the player chooses to exit the game
                    if user1 == "exit":
                        play_game = False
                        break

                    # If the chosen position is already taken
                    elif table[symbols.user_choose[user1]] != " ":
                        print("This position is already taken. Please choose another position.")
                        continue

                    # If the chosen position is available
                    else:
                        # Place the symbol on the chosen position
                        sleep(1)
                        table[symbols.user_choose[user1]] = symbols.cross
                        print(game_manager.show_table(inp_table=table))

                        # Check if the first player wins
                        if symbols.check_winner(table, symbols.cross):
                            print("Congratulations! User1/Cross wins!")
                            play_game = False
                            break

                        # Check if the game ends in a draw
                        if symbols.check_draw(table):
                            print(draw)
                            play_game = False
                            break

                        break  # Exit the loop if the player chose an available position
            except KeyError:
                print("Invalid input. Please choose a valid position.")
                continue

            if not play_game:
                break

            # Loop for the second player's turn
            while True:
                # Check if the second player's choose is valid
                try:
                    user2 = input("User2/Noughts choose your position: ").lower()

                    # If the player chooses to exit the game
                    if user2 == "exit":
                        play_game = False
                        break

                    # If the chosen position is already taken
                    elif table[symbols.user_choose[user2]] != " ":
                        print("This position is already taken. Please choose another position.")
                        continue

                    # If the chosen position is available
                    else:
                        # Place the symbol on the chosen position
                        sleep(1)
                        table[symbols.user_choose[user2]] = symbols.nought
                        print(game_manager.show_table(inp_table=table))

                        # Check if the second player wins
                        if symbols.check_winner(table, symbols.nought):
                            print("Congratulations! User2/Nought wins!")
                            play_game = False
                            break

                        # Check if the game ends in a draw
                        if symbols.check_draw(table):
                            print(draw)
                            play_game = False
                            break

                        break  # Exit the loop if the player chose an available position

                except KeyError:
                    print("Invalid input. Please choose a valid position.")

            if not play_game:
                break

    # If the player chooses to exit the game
    elif play_or_rules == "exit":
        print(goodbye)
        break

    # If the player enters an invalid input
    else:
        print("Invalid input. Please enter 'play' to start the game or 'rules' to see the rules.")
