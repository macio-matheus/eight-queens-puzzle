import time
from random import choice
from collections import Counter
from random import randrange


class EigthQueensPuzzle:
    """
        Model of a state

        State: ([line_queens], (a, b, c), (h))

        a: Store queen column value
        b: Store l-c of queens
        c: Store l+c of queens
        h: Value heuristic of state
        The check is given to each queen of the board,
        where it is tested if there is another queen already
        visited with the same values of a, b, c. If it exists,
        it is not an objective state
    """

    def __init__(self, queens=8):
        self.queens = queens

    def initial(self):
        """
        Initial state
        :return: Initial state from size
        """
        return list(randrange(self.queens) for _ in range(self.queens))

    def heuristic_func(self, state):
        """
        Heurística (h)
        Number of conflicting queen pairs

        :param state:
        :return:
        """
        a, b, c = Counter(), Counter(), Counter()
        # Calculate how many queens are in equal positions
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0
        # scans the count structures (a, b, c) by just increasing the value of the collisions
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def near_states(self, state):
        """
        Neighboring states
        :param state:
        :return: All states accessible from the current moving parts per column
        """
        near_states = []
        # For each state [column] check that neighboring columns are empty
        for row in range(self.queens):
            for col in range(self.queens):
                # If different: then the current col of the iteration is available to move
                # since the state [] stores the value of the columns in which the queens are
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  # Column = column empty
                    near_states.append(list(aux))
        return near_states

    def random_near_state(self, state):
        """
        Random choice state between near states
        :param state: near state list
        :return: a random choice state between near states
        """
        return choice(self.near_states(state))


def hill_climbing(problem):
    # Chama os neighboards com heuristica maior(pois usamos -h)
    current = problem.initial()
    while True:
        neighbours = problem.near_states(current)
        if not neighbours:
            break
        # shuffle(neighbours)
        neighbour = max(neighbours, key=lambda state: problem.heuristic_func(state))
        if problem.heuristic_func(neighbour) <= problem.heuristic_func(current):
            break
        current = neighbour
    return current


def print_board(result):
    """
    Print board
    :param result:
    :return:
    """
    if not result:
        print(None)

    r = choice(result)
    print(r)
    board = []
    for col in r:
        line = ['.'] * len(r)
        line[col] = 'Q'
        board.append(str().join(line))

    charlist = list(map(list, board))
    for line in charlist:
        print(' '.join(line))


def run_search(problem, i):
    """
    Start a search
    :param problem:
    :param i:
    :return: solution
    """
    n_iterations = i
    cnt = 0
    curr_time = lambda: int(round(time.time() * 1000))
    start = curr_time()
    s = []
    for i in range(n_iterations):
        result = hill_climbing(problem)
        if problem.heuristic_func(result) == 0:
            cnt += 1
            s.append(result)
    print(f'- Hit rate:{cnt/n_iterations} \tRuntime: {curr_time() - start}')
    return s


if __name__ == '__main__':
    p = EigthQueensPuzzle()
    result_board = run_search(p, 1000)
    print_board(result_board)
