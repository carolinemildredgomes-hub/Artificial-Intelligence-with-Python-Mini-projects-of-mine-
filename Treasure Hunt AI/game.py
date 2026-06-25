import math

TREASURE = 4


def terminal(state):

    explorer, guardian = state

    return explorer == TREASURE or guardian == TREASURE


def utility(state):

    explorer, guardian = state

    if explorer == TREASURE:
        return 1

    if guardian == TREASURE:
        return -1

    return 0


def actions(state, player):

    explorer, guardian = state

    moves = []

    if player == "Explorer":

        if explorer + 1 <= TREASURE:
            moves.append(explorer + 1)

    else:

        if guardian + 1 <= TREASURE:
            moves.append(guardian + 1)

    return moves


def result(state, move, player):

    explorer, guardian = state

    if player == "Explorer":
        return (move, guardian)

    return (explorer, move)


def max_value(state):

    if terminal(state):
        return utility(state)

    v = -math.inf

    for move in actions(state, "Explorer"):
        v = max(
            v,
            min_value(result(state, move, "Explorer"))
        )

    return v


def min_value(state):

    if terminal(state):
        return utility(state)

    v = math.inf

    for move in actions(state, "Guardian"):
        v = min(
            v,
            max_value(result(state, move, "Guardian"))
        )

    return v


def minimax(state):

    best_score = -math.inf
    best_move = None

    for move in actions(state, "Explorer"):

        score = min_value(
            result(state, move, "Explorer")
        )

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


state = (0, 2)

while not terminal(state):

    explorer, guardian = state

    print("\nCurrent State")
    print(
        f"Explorer={explorer} "
        f"Guardian={guardian} "
        f"Treasure={TREASURE}"
    )

    human_move = int(
        input(
            f"Move Explorer to "
            f"{actions(state,'Explorer')}: "
        )
    )

    state = result(
        state,
        human_move,
        "Explorer"
    )

    if terminal(state):
        break

    ai_move = actions(
        state,
        "Guardian"
    )[0]

    print(
        f"Guardian moves to {ai_move}"
    )

    state = result(
        state,
        ai_move,
        "Guardian"
    )

winner = utility(state)

if winner == 1:
    print("\nExplorer Wins!")

elif winner == -1:
    print("\nGuardian Wins!")
