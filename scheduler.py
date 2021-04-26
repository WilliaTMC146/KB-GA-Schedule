import numpy as np
import random as rd

hari = 365
jr = 450 # jumlah rapat
durasi = []

for i in range(0, jr): # isi durasi
    durasi.append(rd.randrange(1, 9))

#- Class -#
class Schedule:
    def __init__(self):
        self.rapat = [] # hari rapat
        self.durra = [] # durasi rapat per hari
        self.total_durasi_rapat = 0
        self.value = 0
        self.libur = 0
        self.max_ = 0
        self.min_ = 1
        self.ratarata_rapat = 0
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
        self.libur = 0
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
        self.durra[x - 1] = durasi[y]
        self.durra[self.rapat[y] - 1] -= durasi[y]
        self.rapat[y] = x
        #print("Index     :", y)
        #print("Nilai     :", x)
        # return self.rapat

    def check_limit_rapat(self):
        for i in range (0, jr):
            self.durra[self.rapat[i] - 1] = 0

        for i in range (0, jr):
            self.durra[self.rapat[i] - 1] += durasi[i]

    def durra_more_than_limit(self):
        for i in range (0, hari):
            if self.durra[i] > 12:
                return true
        return false

    def get_minmax_rapat(self):
        temp = 0
        for i in range (0,jr):
            temp = self.rapat.count(i)
            if(temp > self.max_):
                self.max_ = temp
            if(temp < self.min_ and temp != 0):
                self.min_ = temp
        
        #print("Rapat Terbanyak dalam 1 hari: ", self.max_)
        #print("Rapat Paling Sedikit dalam 1 hari: ", self.min_)

    def count_libur(self):
        libur = 0
        for i in range(0, hari):
            if self.rapat.count(i) == 0:
                libur +=1

    def set_rapat(self, arra):
        for i in range(0, jr):
            self.rapat[i] = arra[i]

    def get_data_rapat(self, x):
        return self.rapat[x]

    def get_rapat(self):
        return self.rapat

    def set_rapat_index(self,x,y):
        self.rapat[x] = y

    def set_fitness(self, x):
        self.value = x

    def print_rapat(self):
        print(self.rapat)

    def get_average_rapat(self):
        return np.avreage(self.rapat)

    def get_fitness(self):
        return self.value

    def print_fitness(self):
        print(self.value)

    def print_durra(self):
        print(self.durra)

    def print_libur(self):
        print(self.libur)

    def print_hasil(self):
        #print(self.rapat)
        print("Max Rapat: ", self.max_, "  Min Rapat: ", self.min_, "  Rata-Rata Rapat per hari: ", "  Libur: ", self.libur)
        print("Rata-rata Rapat: ", np.average(self.rapat))
        print("Fitness: ", self.value, "\n")

#- Functions -#

def quickSort(array, left, right):
    if left >= right:
        return array
    pivot = array[left].get_fitness()
    i = left + 1
    for j in range(left + 1, right):
        if array[j].get_fitness() > pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1
    temp = array[left]
    array[left] = array[i - 1]
    array[i - 1] = temp
    array = quickSort(array, left, i - 1)
    array = quickSort(array, i, right)
    return array

def sorting(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j].get_fitness() < array[j + 1].get_fitness():
                array[j], array[j + 1] = array[j + 1], array[j]

#- Main -#
pop_value = 5
population = [] # parent
new_gen = [] # generasi baru

for i in range (0, pop_value):
    population.append(Schedule())

#print("== Fitness Function ==")
for i in range (0, pop_value):
    #population[i].print_rapat()
    population[i].fitness_function()
    #print("fitness " + str(i + 1) + " :", end=" ")
    #population[i].print_fitness()

#population = quickSort(population, 0, len(population))
sorting(population)

for gen in range(0,10):
    
    print("Generasi: ", gen + 1)

    # print("\n\n== Fitness Function Sorted ==")
    # for i in range (0, pop_value):
    #     population[i].print_rapat()
    #     print("fitness " + str(i + 1) + " :", end=" ")
    #     population[i].print_fitness()

    #crossover
    #print("\n\n== CrossOver ==")
    for i in range (0, pop_value):
        new_gen.append(Schedule())

    for k in range (0,pop_value):
        s = rd.randrange(0,jr) #start
        ed = rd.randrange(s, jr) #end
        p1 = rd.randrange(0, pop_value) #parent1
        p2 = rd.randrange(0, pop_value) #parent2

        if p1 != p2:
            #print(str(k) + "| P1 :" + str(p1) + " | P2 :" + str(p2))
            for i in range(0, jr):
                if i >= s and i < ed:
                    new_gen[k].set_rapat_index(i, population[p1].get_data_rapat(i))
                else:
                    new_gen[k].set_rapat_index(i, population[p2].get_data_rapat(i))

            #print("new gen for", end=" ")
            #new_gen[k].check_limit_rapat()
            #new_gen[k].fitness_function()
            #new_gen[k].print_fitness()
            # new_gen[k].print_rapat()
            # new_gen[k].print_fitness()

    #print("\n\n== After CrossOver ==")
    #for i in range (0,pop_value):
        #new_gen[i].print_rapat()
        #new_gen[i].print_fitness()

    #new_gen = quickSort(new_gen, 0, len(new_gen))
    sorting(new_gen)

    #print("\n== Penggabungan ==")
    for i in range(0, pop_value):
        mutation_chance = rd.randrange(1, 5)
        if new_gen[i].get_fitness() > population[pop_value - 1].get_fitness():
            population[pop_value - 1] = new_gen[i]
            population = quickSort(population, 0, len(population))
        if mutation_chance == 2:
            #print("population " + str(i))
            #print(population[i].get_rapat())
            population[i].single_mutasi()
            population[i].fitness_function()
        

    #print("\n== New Gen ==")
    #for i in range (0,pop_value):
        #population[i].print_rapat()
        #population[i].print_fitness()

    #population = quickSort(population, 0, len(population))
    sorting(population)

    #print("\n\n== Fitness Function Sorted New Gen ==")
    for i in range (0, pop_value):
        population[i].get_minmax_rapat()
        print("Parent " + str(i + 1) + " :", end=" ")
        population[i].count_libur()
        population[i].print_hasil()

    # population[0].get_minmax_rapat()
    # population[0].count_libur()
    # population[0].average_rapat()
    # population[0].print_hasil()

    print("\n")
    