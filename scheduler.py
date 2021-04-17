import numpy as np
import random as rd

hari = 8
jr = 10
durasi = []

for i in range(1, jr): #durasi
    durasi.append(rd.randrange(1, 8))

#- Class -#
class Schedule:
    def __init__(self):
        self.rapat = []
        self.durra = [] #durasi rapat per hari
        self.fitness = 0
        self.total_durasi_rapat = 0
        self.value = 0
        self.libur = 0

        for i in range(0,jr):
            self.durra.append(0)

        #for i in range(0, jr):
            #x = rd.randrange(1, hari)
            #self.rapat.append(x)

        j = 1
        while j < jr:
            x = rd.randrange(1, hari)
            if self.durra[x] + durasi[j] < 12:
                self.durra[x] = self.durra[x] + durasi[j]
                self.rapat.append(x)
                j += 1
            else:
                continue


    def fitness_function(self):
        sum_total_rapat = 0
        self.total_durasi_rapat = (np.sum(self.rapat) * 2)
        for i in range(1, hari):
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

    def print_durra(self):
        print(self.durra)

#- Functions -#
def fitness_function():
    pass

def rand_durasi(durasi):
    pass

#- Main -#
#durasi = []
pop_value = 5
population = [] #parent
new_gen = [] #generasi baru

for i in range (0, pop_value):
    population.append(Schedule())

for i in range (0, pop_value):
    population[i].print_rapat()

population[0].fitness_function()


print(durasi)