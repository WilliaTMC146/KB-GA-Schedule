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
        # print(self.value)

    def get_crossover(self):
        result = 0
        start = 2
        end = 5
        i = 0
        array = []

        for i in range(start, end):
            array.append(self.rapat[i])
        
        return array

    def single_mutasi(self):
        x = rd.randrange(1, hari)
        y = rd.randrange(0, jr)
        while self.durra[x - 1] + durasi[y] > 12:
            x = rd.randrange(1, hari)
        self.durra[x-1] = durasi[y]
        self.durra[self.rapat[y] - 1] -= durasi[y]
        self.rapat[y] = x
        print("Index     :", y)
        print("Nilai     :", x)
        return self.rapat

    def check_limit_rapat(self):
        for i in range (0, jr):
            self.durra[self.rapat[i] - 1] = 0

        for i in range (0, jr):
            self.durra[self.rapat[i] - 1] += durasi[i]

    def set_rapat(self, arra):
        for i in range(0, jr):
            self.rapat[i] = arra[i]

    def get_data_rapat(self, x):
        return self.rapat[x]

    def print_rapat(self):
        print(self.rapat)

    def get_fitness(self):
        return self.value

    def print_fitness(self):
        print(self.value)

    def print_durra(self):
        print(self.durra)

#- Functions -#

#- Main -#
pop_value = 10
population = [] # parent
new_gen = [] # generasi baru

for i in range (0, pop_value):
    population.append(Schedule())

print("== Fitness Function ==")
for i in range (0, pop_value):
    # population[i].print_rapat()
    population[i].fitness_function()
    print("fitness " + str(i + 1) + " :", end=" ")
    population[i].print_fitness()

print("\n== Crossover ==")
print("durasi    :", durasi)
print("parent [0]:", end=" ")
population[0].print_rapat()
print("parent [3]:", end=" ")
population[3].print_rapat()

arr = population[0].get_crossover()
print("crossover from parent [0] :", arr)

for i in range(0, 10):
    if i >= 2 and i < 5:
        new_gen.append(population[0].get_data_rapat(i))
    else:
        new_gen.append(population[3].get_data_rapat(i))

print("new_gen   :", new_gen)

# print("crossover:",end=" ")
# population[0].set_rapat(new_gen)

print("\n== Mutation ==")
print("parent [0]:", end=" ")
population[0].print_rapat()
print("mutasi    :", population[0].single_mutasi())

population[0].fitness_function()
print("fitness   :", end=" ")
population[0].print_fitness()

population[0].check_limit_rapat()
print("Durra     :", end=" ")
population[0].print_durra()

# population.append(new_gen)
# print("new parent:", end=" ")
# population[10].print_rapat()