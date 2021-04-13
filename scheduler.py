import numpy as np
import random as rd

#- Class -#
class Schedule:
    def __init__(self):
        self.rapat = []
        self.fitness = 0
        self.total_durasi_rapat = 0
        self.value = 0
        self.libur = 0

        for i in range(0, 10):
            self.rapat.append(rd.randrange(1, 8))

    def fitness_function(self):
        sum_total_rapat = 0
        self.total_durasi_rapat = (np.sum(self.rapat) * 2)
        for i in range(1, 8):
            if self.rapat.count(i) == 0:
                self.libur += 1
            sum_total_rapat += 2**self.rapat.count(i)
        self.value = self.total_durasi_rapat + sum_total_rapat + self.libur
        # print(self.total_durasi_rapat)
        # print(sum_total_rapat)
        # print(self.libur)
        print(self.value)

    def print_rapat(self):
        print(self.rapat)

    def get_fitness(self):
        return self.fitness

    def print_fitness(self):
        print(self.fitness)

    def set_meet_hour():
        pass

#- Functions -#
def fitness_function():
    pass

def rand_durasi(durasi):
    for i in range(1, 10):
        durasi.append(rd.randrange(1, 8))

#- Main -#
durasi = []
pop_value = 5
population = []

for i in range (0, pop_value):
    population.append(Schedule())

for i in range (0, pop_value):
    population[i].print_rapat()

population[0].fitness_function()