import statistics
from statistics import variance, mean
import math
from fitness import FitnessFunction
from srtm.utilities import SRTM1_DIR

import random

f = FitnessFunction()


def schedule(temp, k, alpha=0.9999999):
    return  temp * (alpha ** k)


def simulated_annealing (x,y):

    #defining variables
    current = (x,y)
    t = 1
    v = 0.39
    k = 0

    best_solution = current


    while True:


        if (t <= 0):
            return best_solution

        next_x = random.normalvariate(current[0], v)  # Perturb latitude
        next_y = random.normalvariate(current[1], v)

        # Perturb longitude



        next = (next_x, next_y)  #fix this
        if f(next)  is None:
            continue


        deltaE = f(next) - f(current)
        #
        # if new value is greater than current value then we ALWAYS choose it
        if (deltaE > 0):
            current = next

        else:

            probability = math.exp(deltaE / (t))
            random_chance = random.uniform(0, 1)

            if random_chance < probability:
                current = next
        if(f(next) > f(best_solution)):
            best_solution = next

        print(f"current: {current} altitude: {f(current)}")
        k += 1
        t = schedule(t, k)



sol = simulated_annealing(46.8, -92.08)
print(f"solution: {sol} altitude: {f(sol)}")


