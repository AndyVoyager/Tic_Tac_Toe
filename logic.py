__author__ = "AndyVoyager"


class Game:

    def __init__(self):
        self.table = []
        self.cross = "X"
        self.nought = "O"
        self.null = " "

    def create_table(self):
        # Create the self.table:
        for i in range(6):

            for j in range(14):
                # Add the letters:
                if i == 0:
                    if j == 3:
                        self.table.append("A")
                    elif j == 7:
                        self.table.append("B")
                    elif j == 11:
                        self.table.append("C")
                    else:
                        self.table.append(" ")

                # Add the numbers:
                if i % 2 != 0:
                    if j == 0 and i == 1:
                        self.table.append("1")
                    elif j == 0 and i == 3:
                        self.table.append("2")
                    elif j == 0 and i == 5:
                        self.table.append("3")

                    # Add the vertical lines:
                    else:
                        if j == 1 or j == 5 or j == 9 or j == 13:
                            self.table.append("|")
                        else:
                            self.table.append(" ")

                # Add the horizontal lines:
                else:
                    if i != 0:
                        if j == 0:
                            self.table.append(" ")
                        else:
                            self.table.append("-")

            self.table.append("\n")

        # self.table = "".join(map(str, self.table))
        return self.table

    def show_table(self, inp_table):
        self.table = "".join(map(str, inp_table))
        return self.table


class Symbols:

    def __init__(self):
        # Initialise the positions of the symbols:
        self.a1 = 18
        self.b1 = 22
        self.c1 = 26
        self.a2 = 48
        self.b2 = 52
        self.c2 = 56
        self.a3 = 78
        self.b3 = 82
        self.c3 = 86

        self.user_choose = {
            "a1": self.a1,
            "b1": self.b1,
            "c1": self.c1,
            "a2": self.a2,
            "b2": self.b2,
            "c2": self.c2,
            "a3": self.a3,
            "b3": self.b3,
            "c3": self.c3
        }

        # Initialise the symbols:
        self.cross = "X"
        self.nought = "O"

    def check_winner(self, table, symbol):
        # Check horizontals:
        if (table[self.a1] == table[self.b1] == table[self.c1] == symbol or
                table[self.a2] == table[self.b2] == table[self.c2] == symbol or
                table[self.a3] == table[self.b3] == table[self.c3] == symbol):
            return True

        # Check verticals:
        if (table[self.a1] == table[self.a2] == table[self.a3] == symbol or
                table[self.b1] == table[self.b2] == table[self.b3] == symbol or
                table[self.c1] == table[self.c2] == table[self.c3] == symbol):
            return True

        # Check diagonals:
        if (table[self.a1] == table[self.b2] == table[self.c3] == symbol or
                table[self.a3] == table[self.b2] == table[self.c1] == symbol):
            return True

        return False

    def check_draw(self, table):
        for key in self.user_choose:
            if table[self.user_choose[key]] == " ":
                return False
        return True
