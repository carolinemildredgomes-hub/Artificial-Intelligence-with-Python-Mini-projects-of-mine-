import csv
from collections import deque

stations = {}
connections = {}


def load_data():

    with open("stations.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            stations[row["id"]] = row["name"]
            connections[row["id"]] = []

    with open("connections.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:

            a = row["station1"]
            b = row["station2"]

            connections[a].append(b)
            connections[b].append(a)


def bfs(start, goal):

    queue = deque()

    queue.append(start)

    visited = set()

    visited.add(start)

    parent = {}

    while queue:

        current = queue.popleft()

        if current == goal:

            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)

            path.reverse()

            return path

        for neighbor in connections[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    return None


load_data()

start_name = input("Start Station: ")
goal_name = input("Destination Station: ")

start = None
goal = None

for station_id, name in stations.items():

    if name.lower() == start_name.lower():
        start = station_id

    if name.lower() == goal_name.lower():
        goal = station_id

if start is None or goal is None:
    print("Station not found.")
else:

    path = bfs(start, goal)

    if path is None:
        print("No route found.")

    else:

        print("\nShortest Route:\n")

        for station in path:
            print(stations[station])

        print(f"\nStops: {len(path) - 1}")
