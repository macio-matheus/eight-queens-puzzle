import time
from random import choice
from collections import Counter
from random import randrange


class EigthQueensPuzzle:
    # Modelo de um estado
    #
    # State: ([line_queens],
    #        (a, b, c),
    #        (h)
    #
    # Onde:
    # a: guarda o valor da coluna das rainhas
    # b: guarda l-c das rainhas
    # c: guarda l+c das rainhas
    # h: valor da heuristica do estado
    # A verificacao se da para cada rainha do tabuleiro, onde e testado
    # se existe outra rainha ja visitada com os mesmos valores de a,b,c.
    # caso exista, nao e um estado objetivo

    def __init__(self, n_queens=8):
        self.n_queens = n_queens

    # Estado inicial:
    #   Retorna o estado inicial a partir do size
    def initial(self):
        return list(randrange(self.n_queens) for _ in range(self.n_queens))

    # Heuristica: h
    #   Numero de pares de rainhas se atacando
    def heuristic_func(self, state):
        """
        Heurística (h)

        :param state:
        :return:
        """
        # define a,b,c como contadores
        a, b, c = Counter(), Counter(), Counter()
        # contar quantas rainhas tem os valores (a,b,c)
        # de forma que se obtem por exemplo quantas rainhas tem o valor de a=1
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0  # inicia as colisoes com 0
        # varre as estruturas de contagem (a,b,c) apenas incrementando o valor das colisoes
        # caso para algum valor de (a/b/c)>1 ja que e feito cnt[key]-1
        # divide para retirar contagens dobradas
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def near_states(self, state):
        """
        Estados vizinhos
        :param state:
        :return: Todos os estados acessiveis a partir do atual movendo as pecas por coluna
        """
        near_states = []
        # Para cada state[coluna] verfica se as colunas vizinhas estao vazias
        for row in range(self.n_queens):
            for col in range(self.n_queens):
                # Se for diferente:
                #   entao a col atual da iteracao esta disponivel para movimentar-se
                #   visto que o state[] guarda o valor das colunas em que estao as rainhas
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  # Troca a coluna para a vazia
                    near_states.append(list(aux))  # E inclui na lista de near_states
        return near_states

    # Retorna uma escolha aleatoria dentre os estados proximos
    def random_near_state(self, state):
        return choice(self.near_states(state))


curr_time = lambda: int(round(time.time() * 1000))


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
    n_iterations = i
    cnt = 0
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
