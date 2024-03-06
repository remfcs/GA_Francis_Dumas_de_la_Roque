# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities as ci
import random as rd

class TSProblem(GAProblem):
    def list_chromosome(self):
        """
        Description : Create the chromosomes composed by cities
        Argument: No arguments
        Return: chromosome ([])
        """
        chromosome = ci.default_road(city_dict)
        chromosome = rd.sample(chromosome, len(chromosome)) 
        return chromosome 
    
    def evaluate_fitness(self, chromosome):
        """
        Description : Evaluate the fitness of the chromosome given in argument
        Argument: chromosome ([])
        Return: fitness (int) 
        """
        fitness = -ci.road_length(city_dict, chromosome) 
        return fitness 
    
    def merge(self, parent_a, parent_b):
        """
        Description: This function takes a first chromosome and split it to keep the first part.
                     Then it takes the second chromosome to complete the new chromosome created.
        Argument:    2 chromosomes ([])
        Return:      chromosome ([])
        """
        
        x_point = len(parent_a.chromosome)//2
        # New chrom is created from the first genes of parent_a until the x_point one
        new_chrom = parent_a.chromosome[0:x_point]
    
        # To avoid duplicate, we test if each gene of the parent_b from the x_point already exists in the new chrom
        for x_point in range(len(parent_b.chromosome)):
            if parent_b.chromosome[x_point] not in new_chrom:
                new_chrom.append(parent_b.chromosome[x_point])
        return new_chrom
    
    def mutation(self, new_chrom):
        """
        Description: This function takes 2 random genes of the chromosome and exchanges their position randomly
        Argument:    chromosome ([])
        Return:      chromosome ([])
        """
        city_a = ""
        city_b = ""
        while city_a == city_b:
            city_a = rd.choice(new_chrom)
            city_b = rd.choice(new_chrom)
        
        # We seek the index of city_a and city_b to invert them
        index_city_a = new_chrom.index(city_a)
        index_city_b = new_chrom.index(city_b)
        new_chrom[index_city_a], new_chrom[index_city_b] = city_b, city_a
        return new_chrom

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = ci.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    ci.draw_cities(city_dict, solver.get_best_individual().chromosome)
