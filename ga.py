"""
Examples:
    $ python3 ga.py --crossover 1X (Single point crossover)
    $ python3 ga.py --crossover uniform (Uniform crossover)
    $ python3 ga.py --mutation-rate 0.1 (Mutation rate = 10%)
    $ python3 ga.py --population-size 100 (Population size = 100)
"""

import sys
import random
from copy import copy
from string import digits, ascii_letters

alphabet = ascii_letters + digits + ' '

def tournament(population, target, n):
    result= []
    while len(result) < n:
        child1 = random.choice(population)
        child2 = random.choice(population)
        if fitness(child1, target) > fitness(child2, target):
            result.append(child1)
            population.remove(child1)
        else:
            result.append(child2)
            population.remove(child2)

    return result


def single_point_crossover(parent1, parent2):
    child1 = copy(parent1)
    child2 = copy(parent2)
    split_point = random.randint(1, len(parent1) - 1)
    for i in range(len(parent1)):
        if i < split_point:
            child1[i] = parent2[i]
        else:
            child2[i] = parent1[i]

    return child1, child2

def uniform_crossover(parent1, parent2):
    child1 = []
    child2 = []
    for i, j in enumerate(parent1):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return child1, child2


def mutation(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index]= random.choice(alphabet)

    return individual


def fitness(message, target):
    value = 0
    for i, actual in enumerate(target):
        value += 1 if message[i] == actual else 0

    return value

def evaluate(population, target):
    fitness_values = []
    for individual in population:
        fitness_values.append(fitness(individual, target))

    return fitness_values

def selection(population, fitness_values):
    results = []
    while len(results) < 2:
        choice = random.randint(0, sum(fitness_values))
        for i, value in enumerate(fitness_values):
            choice -= value
            if choice < 0:
                results.append(population[i])

    return results[0], results[1]


def arg_max(numbers):
    max_index = None
    max_value = -sys.maxsize - 1
    for i, value in enumerate(numbers):
        if value > max_value:
            max_index = i
            max_value = value

    return max_index, max_value


if __name__ == "__main__":

    import time
    import argparse

    parser = argparse.ArgumentParser(description="Evolve a sentence with Genetic Algorithm")
    parser.add_argument("--target", type=str, default="METHINKS IT IS LIKE A WEASEL")
    parser.add_argument("--mutation-rate", "-m", type=float, default=0.01)
    parser.add_argument("--population-size", "-p", type=int, default=180)
    parser.add_argument("--crossover", "-c", choices=("1X", "uniform"), type=str, default="uniform")
    args = parser.parse_args()

    crossover_operators = {
        "1X": single_point_crossover,
        "uniform": uniform_crossover
    }

    population = []
    target = args.target
    mutation_rate = args.mutation_rate
    population_size = args.population_size
    crossover = crossover_operators[args.crossover]
    for i in range(population_size):
        message = [random.choice(alphabet) for _ in range(len(target))]
        population.append(message)

    counter = 0
    print("Target = {}\n".format(target))

    while True:
        counter += 1
        fitness_values = evaluate(population, target)
        max_index, max_value = arg_max(fitness_values)
        best = ''.join(population[max_index])
        print("Generation {}: {} ({})".format(counter, best, max_value))

        if best == target:
            break

        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = selection(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                mutation(child1)
            if random.random() < mutation_rate:
                mutation(child2)

            new_population.append(child1)
            new_population.append(child2)

        population = tournament(population + new_population, target, population_size)
