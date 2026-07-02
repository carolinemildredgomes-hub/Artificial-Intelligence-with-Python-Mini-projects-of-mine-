import csv
import itertools

PROBS = {
    "group": {
        "action": 0.3,
        "romance": 0.3,
        "mixed": 0.2,
        "none": 0.2
    }
}


def load_data(filename):
    data = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["name"]] = {
                "action": int(row["likes_action"]),
                "romance": int(row["likes_romance"])
            }
    return data


def powerset(s):
    s = list(s)
    return [set(x) for i in range(len(s)+1)
            for x in itertools.combinations(s, i)]


def joint_probability(people, action_group):
    p = 1

    for person in people:

        likes_action = person in action_group

        if likes_action:
            p *= 0.7
        else:
            p *= 0.3

    return p


def update(probabilities, action_group, p):
    for person in probabilities:
        probabilities[person]["action"][person in action_group] += p


def normalize(probabilities):
    for person in probabilities:
        total = sum(probabilities[person]["action"].values())
        for val in probabilities[person]["action"]:
            probabilities[person]["action"][val] /= total


def main():
    people = load_data("data/users.csv")

    probabilities = {
        person: {"action": {True: 0, False: 0}}
        for person in people
    }

    names = set(people)

    for action_group in powerset(names):
        p = joint_probability(people, action_group)
        update(probabilities, action_group, p)

    normalize(probabilities)

    for person in probabilities:
        print(person, probabilities[person])


if __name__ == "__main__":
    main()
