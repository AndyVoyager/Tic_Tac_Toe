__author__ = "AndyVoyager"

welcome = ("""
 __        __   _                            _         _____ _         _____             _____          _ 
 \\ \\      / /__| | ___ ___  _ __ ___   ___  (_)_ __   |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___| |
  \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | | '_ \\    | | | |/ __|____| |/ _` |/ __|____| |/ _ \\ / _ \\ |
   \\ V  V /  __/ | (_| (_) | | | | | |  __/ | | | | |   | | | | (_|_____| | (_| | (_|_____| | (_) |  __/_|
    \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___| |_|_| |_|   |_| |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___(_)

""")

goodbye = """
   ____                 _ _                _ 
  / ___| ___   ___   __| | |__  _   _  ___| |
 | |  _ / _ \\ / _ \\ / _` | '_ \\| | | |/ _ \\ |
 | |_| | (_) | (_) | (_| | |_) | |_| |  __/_|
  \\____|\\___/ \\___/ \\__,_|_.__/ \\__, |\\___(_)
                                |___/        """

start = """
  _         _   _           _             _     _   _                                         _ 
 | |    ___| |_( )___   ___| |_ __ _ _ __| |_  | |_| |__   ___    __ _  __ _ _ __ ___   ___  | |
 | |   / _ \\ __|// __| / __| __/ _` | '__| __| | __| '_ \\ / _ \\  / _` |/ _` | '_ ` _ \\ / _ \\ | |
 | |__|  __/ |_  \\__ \\ \\__ \\ || (_| | |  | |_  | |_| | | |  __/ | (_| | (_| | | | | | |  __/ |_|
 |_____\\___|\\__| |___/ |___/\\__\\__,_|_|   \\__|  \\__|_| |_|\\___|  \\__, |\\__,_|_| |_| |_|\\___| (_)
                                                                 |___/                          
"""

draw = """
  ___ _   _                   _                      _ 
 |_ _| |_( )___    __ _    __| |_ __ __ ___      __ | |
  | || __|// __|  / _` |  / _` | '__/ _` \\ \\ /\\ / / | |
  | || |_  \\\\_\\__ \\ | (_| | | (_| | | | (_| |\\ V  V /  |_|
 |___|\\\\__| |___/  \\__,_|  \\__,_|_|  \\__,_| \\_/\\_/   (_)                                                       
"""


rules = """
Board:          The game is played on a square board consisting of 3x3 squares.
Positions:      Each square on the board has a unique position, identified by a combination of a column letter 
                (a, b, or c) and a row number (1, 2, or 3). For example, "a1" represents the top-left corner of the 
                board, and "c3" represents the bottom-right corner.
Player Turns:   Players take turns selecting a position on the board to place their symbol. The first player starts.
Player Symbols: The first player uses the symbol "X", and the second player uses the symbol "O".
Winning:        A player wins the game by placing three of their symbols in a row horizontally, vertically, or
                diagonally. If all squares on the board are filled and no player achieves a winning combination, 
                the game ends in a draw.
Invalid Inputs: If a player enters an invalid position, such as "d2" or "b4", the game notifies the player of the error
                and prompts them to enter a valid position.
End of Game:    The game concludes when one player wins or when all squares on the board are filled without a winner.
                After the game ends, players may choose whether they want to start a new game.
                
Now, with the rules in mind, players can enjoy playing Tic-Tac-Toe!
"""
