class KnowledgeBase:


    def __init__(self):

        self.safe_cells = set()

        self.obstacles = set()



    def add_safe(self, cell):

        self.safe_cells.add(cell)



    def add_obstacle(self, cell):

        self.obstacles.add(cell)



    def is_safe(self, cell):

        return cell in self.safe_cells



    def show(self):

        print("\nRobot Knowledge:")


        print("Safe Cells:")

        print(self.safe_cells)


        print("Obstacles:")

        print(self.obstacles)
