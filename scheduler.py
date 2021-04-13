import numpy as np
import random as rd

#- Global Variable -#
durasi = []
libur = 0
#- Class -#
class Schedule:
    rapat = []
    fitness = 0

    # coba2
    total_rapat = 0

    def __init__(self):
        for i in range(1, 10):
            self.rapat.append(rd.randrange(1, 7))
        print(self.rapat)
    
    def fitness_function(self):
        self.fitness = (np.sum(self.rapat) * 2) 
        for i in range(1,7):
            if self.rapat.count(i) == 0:
                libur+=1
            self.fitness += 2**self.rapat.count(i)
        self.fitness += libur
        print(self.fitness)

    def get_fitness():
        return fitness

    def set_meet_hour():
        pass

#- Functions -#
def fitness_function():
    pass

def rand_durasi(durasi):
    for i in range(1, 10):
        durasi.append(rd.randrange(1, 7))

#- Main -#
pop_value = 5

population = []

for i in range (1,pop_value):
    population.append(Schedule())

population[3].fitness_function()
