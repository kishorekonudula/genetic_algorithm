# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:52:00 2017

@author: kkonudul
"""

from random import randint

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


