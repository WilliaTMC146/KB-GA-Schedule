import numpy as np
import random as rd

hari = 8
jr = 10 # jumlah rapat
durasi = []

for i in range(0, jr): # isi durasi
    durasi.append(rd.randrange(1, 9))

#- Class -#
class Schedule:
    def __init__(self):
        self.rapat = []
        self.durra = [] # durasi rapat per hari
        self.total_durasi_rapat = 0
        self.value = 0
        self.libur = 0

        for i in range(1, hari):
            self.durra.append(0)

        # for i in range(0, jr):
        #     x = rd.randrange(1, hari)
        #     self.rapat.append(x)

        j = 0
        while j < jr:
            x = rd.randrange(0, hari - 1)
            if self.durra[x] + durasi[j] < 12:
                self.durra[x] = self.durra[x] + durasi[j]
                self.rapat.append(x + 1)
                j += 1
            else:
                continue

    def fitness_function(self):
        sum_total_rapat = 0
        self.total_durasi_rapat = (np.sum(self.durra) * 2)
        for i in range(1, hari):
            if self.rapat.count(i) == 0:
                self.libur += 1
            sum_total_rapat += 2**self.rapat.count(i)
        self.value = self.total_durasi_rapat + sum_total_rapat + self.libur
        # print(self.total_durasi_rapat)
        # print(sum_total_rapat)
        # print(self.libur)
        print(self.value)

    def get_crossover(self):
        result = 0
        start = 2
        end = 5
        i = 0
        array = []

        for i in range(start, end):
            array.append(self.rapat[i])
        
        return array

    def get_data_rapat(self, x):
        return self.rapat[x]

    def print_rapat(self):
        print(self.rapat)

    def get_fitness(self):
        return self.fitness

    def print_fitness(self):
        print(self.fitness)

    def print_durra(self):
        print(self.durra)

#- Functions -#

#- Main -#
pop_value = 5
population = [] # parent
new_gen = [] # generasi baru

for i in range (0, pop_value):
    population.append(Schedule())

for i in range (0, pop_value):
    population[i].print_rapat()
    population[i].fitness_function()

arr = population[0].get_crossover()
print(arr)

for i in range(0, 10):
    if i >= 2 and i < 5:
        new_gen.append(population[0].get_data_rapat(i))
    else:
        new_gen.append(population[3].get_data_rapat(i))

print("new_gen :", new_gen)

#print(durasi)