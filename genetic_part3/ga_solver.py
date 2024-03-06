# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random as rd
import mastermind as mm

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Those function will be called in the under classes MasterMindProblem and TSProblem beacause they are different depending on the problem"""
    
    def list_chromosome(self):
        pass
    
    def evaluate_fitness(self, chromosome):
        pass
    
    def merge(self, population, parent_a_index, parent_b_index): 
        pass
        
    def mutation(self, population, Index):
        pass



class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals
            - Argument: The population size can be specified.
        """
        for i in range(pop_size):
            #create each chromosome, evaluate its fitness and add it in the population as an invidual
            chromosome = self._problem.list_chromosome()
            fitness = self._problem.evaluate_fitness(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        self._population.sort(reverse=True) # Selection 
        elements_supp = int(len(self._population)*self._selection_rate)
        self._population = self._population[:-elements_supp] #delete x% of the population
        
        #replace each individual remove by a new one
        for i in range(elements_supp):
            #Find parent_a and parent_b that will be merge
            num_parent_a = 0
            num_parent_b = 0
            while num_parent_a == num_parent_b:
                num_parent_a = rd.randrange(0, len(self._population))
                num_parent_b = rd.randrange(0, len(self._population))
            parent_a, parent_b = self._population[num_parent_a], self._population[num_parent_b]
            
            #Merge them
            new_chrom = self._problem.merge(parent_a, parent_b)
            new_individual = Individual(new_chrom, self._problem.evaluate_fitness(new_chrom))
            
            # Mutation
            number = rd.random()
            if number < self._mutation_rate: 
                new_chrom = self._problem.mutation(new_chrom)
                new_individual = Individual(new_chrom, self._problem.evaluate_fitness(new_chrom))
                
            #Add the new invidual in the population
            self._population.append(new_individual)


    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        for i in range(max_nb_of_generations):
            self.evolve_for_one_generation()
            self._population.sort(reverse=True)
            # print(f"gen {i}")
            if threshold_fitness is not None:
                if self._population[0].fitness >= threshold_fitness:
                    break           
