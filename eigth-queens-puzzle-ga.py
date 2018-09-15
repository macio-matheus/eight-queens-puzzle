import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import numpy as np


def evaluator(individual: list):
    """
    Count the number of conflicts on each diagonal
    :param individual:
    :return: num conflicts
    """
    size = len(individual)
    left_diagonal = [0] * (2 * size - 1)
    right_diagonal = [0] * (2 * size - 1)

    # Sum the number of queens on each diagonal:
    for i in range(size):
        left_diagonal[i + individual[i]] += 1
        right_diagonal[size - 1 - i + individual[i]] += 1

    sum_ = 0
    for i in range(2 * size - 1):
        if left_diagonal[i] > 1:
            sum_ += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            sum_ += right_diagonal[i] - 1
    return sum_,


def view_solution(hof):
    board = (np.zeros((8, 8), dtype=np.int)).tolist()

    for line in range(len(hof)):
        board[line][hof[line]] = 1
    return board


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(8), 8)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluator)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=5)


def main():
    random.seed(0)

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", np.mean)
    stats.register("Std", np.std)
    stats.register("Min", np.min)
    stats.register("Max", np.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=False)

    return pop, stats, hof


pop, stats, hof = main()
view_solution(hof[0])
