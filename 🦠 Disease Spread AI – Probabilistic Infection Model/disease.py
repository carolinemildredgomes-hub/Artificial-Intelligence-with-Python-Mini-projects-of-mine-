import csv
import itertools

PROBS = {
    "infection": 0.2,
    "spread": 0.6
}


def load_data(filename):
    data = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts = set(row["contacts"].split(";")) if row["contacts"] else set()
            data[row["name"]] = {
                "contacts": contacts,
                "infection": (True if row["infection"] == "1"
                              else False if row["infection"] == "0"
                              else None)
            }
    return data


def powerset(s):
    s = list(s)
    return [set(x) for i in range(len(s)+1)
            for x in itertools.combinations(s, i)]


def joint_probability(people, infected_set):
    p = 1

    for person in people:

        infected = person in infected_set
        contacts = people[person]["contacts"]

        if not contacts:
            infection_prob = PROBS["infection"]
        else:
            infected_contacts = len(contacts & infected_set)
            infection_prob = 1 - ((1 - PROBS["spread"]) ** infected_contacts)

        if infected:
            p *= infection_prob
        else:
            p *= (1 - infection_prob)

    return p


def update(probabilities, infected_set, p):
    for person in probabilities:
        probabilities[person]["infection"][person in infected_set] += p


def normalize(probabilities):
    for person in probabilities:
        total = sum(probabilities[person]["infection"].values())
        for val in probabilities[person]["infection"]:
            probabilities[person]["infection"][val] /= total


def main():
    people = load_data("data/community0.csv")

    probabilities = {
        person: {"infection": {True: 0, False: 0}}
        for person in people
    }

    names = set(people)

    for infected_set in powerset(names):
        p = joint_probability(people, infected_set)
        update(probabilities, infected_set, p)

    normalize(probabilities)

    for person in probabilities:
        print(person, probabilities[person])


if __name__ == "__main__":
    main()
