# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:52:00 2017

@author: kkonudul
"""

from random import randint, random
import matplotlib.pyplot as plt

def individual(length, min, max):
    return [randint(min, max) for x in range(length)]

#individual(5, 0,100)

def population(count, length, min, max):
#     Create a number of individuals (i.e. a population).

#     count: the number of individuals in the population
#     length: the number of values per individual
#     min: the min possible value in an individual's list of values
#     max: the max possible value in an individual's list of values

     return [individual(length, min, max) for x in range(count)]

#population(3, 5, 0, 100)

def fitness(individual, target):

#     Determine the fitness of an individual. Lower is better.
#
#     individual: the individual to evaluate
#     target: the sum of numbers that individuals are aiming for
    sm = sum(individual)
    return abs(target-sm)

#fitness([62, 8, 61, 74, 18], 200)

def grade(pop, target):
    #'Find average fitness for a population.'
    # Calculate the total fitness score of all the individuals in the population and average 
    pop_total = sum([fitness(p, target) for p in pop])
    return pop_total / (len(pop) * 1.0)

def evolve(pop, target, min, max, retain = 0.2, random_select = 0.05, mutate = 0.01):
    # retain is used to select the top parents
    # random_select is used to select individuals ransomly to maintain genetic diversity
    # mutate is used to mutate individuals
    # min and max are the numbers used to create the population
    
    # Get the fitness score for each infividual in the population
    graded = [(fitness(x, target), x) for x in pop]
    # Sort the individuals based on the fitness score and drop the fitness score. Our fitness score is calculated 
    # so that the least is the best. If we calculated the score to be highest best, then we would sort in reverse.
    graded = [x[1] for x in sorted(graded)]
    # Getting the index to select the parents and select those individuals from the population
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    
    # Randomly add other elements to promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual) - 1)
            individual[pos_to_mutate] = randint(min, max)
    
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length - 1)
        female = randint(0, parents_length - 1)
        if male != female:
            # Getting the male and female from the positions we got earlier
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)
    parents.extend(children)
    return parents

# Main code to run the program
target = 200
p_count = 100
i_length = 5
i_min = 0
i_max = 100
iterations = 100
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target)]
for i in range(iterations):
    p = evolve(p, target, i_min, i_max)
    fitness_history.append(grade(p, target))

plt.plot(fitness_history)
plt.xlabel('Evolution curve')
plt.show()