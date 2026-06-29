class Environment:


    def __init__(self, filename):

        self.grid = []

        self.start = None
        self.goal = None


        with open(filename, "r") as file:


            for i, line in enumerate(file):

                row = line.strip().split()


                for j, value in enumerate(row):

                    if value == "S":

                        self.start = (i, j)


                    elif value == "G":

                        self.goal = (i, j)


                self.grid.append(row)



    def display(self):

        for row in self.grid:

            print(" ".join(row))



    def is_valid(self, position):

        i, j = position


        if i < 0 or j < 0:

            return False


        if i >= len(self.grid):

            return False


        if j >= len(self.grid[0]):

            return False


        if self.grid[i][j] == "X":

            return False


        return True



    def neighbors(self, position):

        i, j = position


        moves = [

            (i-1, j),   # up
            (i+1, j),   # down
            (i, j-1),   # left
            (i, j+1)    # right

        ]


        safe = []


        for move in moves:


            if self.is_valid(move):

                safe.append(move)



        return safe
