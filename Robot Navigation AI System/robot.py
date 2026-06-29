from environment import Environment
from knowledge import KnowledgeBase



def robot_navigation(filename):


    env = Environment(filename)


    knowledge = KnowledgeBase()



    current = env.start


    goal = env.goal



    visited = set()


    path = []



    print("Robot Starting...\n")



    while current != goal:


        visited.add(current)

        path.append(current)



        print("Current Position:", current)



        possible_moves = env.neighbors(current)



        next_move = None



        for move in possible_moves:


            knowledge.add_safe(move)


            if move not in visited:


                next_move = move

                break



        if next_move is None:

            print("No path found")

            return



        print("Moving to:", next_move)

        print()


        current = next_move



    path.append(goal)



    print("\nGoal Reached!")



    print("\nFinal Path:")


    for step in path:

        print(step)




if __name__ == "__main__":


    robot_navigation("data/map1.txt")
