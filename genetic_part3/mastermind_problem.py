# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm
import random as rd


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def list_chromosome(self):
        """
        Description : Create the chromosomes composed by colors
        Argument: No arguments
        Return: chromosome ([])
        """
        
        chromosome = match.generate_random_guess()  
        return chromosome 
    
    def evaluate_fitness(self, chromosome):
        """
        Description : Evaluate the fitness of the chromosome given in argument
        Argument: chromosome ([])
        Return: fitness (int) 
        """
        fitness = match.rate_guess(chromosome) 
        return fitness 
    
    def merge(self, parent_a, parent_b):
        """
        Description: This function takes a first chromosome and split it randomly to keep the first part.
                     Then it takes the second chromosome to complete the new chromosome created.
        Argument:    2 chromosomes ([])
        Return:      chromosome ([])
        """
        x_point = rd.randrange(0,len(parent_a.chromosome)) 
        new_chrom = parent_a.chromosome[0:x_point] + parent_b.chromosome[x_point:] 
        return new_chrom
        
    def mutation(self, new_chrom):
        """
        Description: This function takes a random position of the chromosome and mutate its gene randomly 
        Argument:    chromosome ([])
        Return:      chromosome ([])
        """
        valid_colors = mm.get_possible_colors()
        new_gene = rd.choice(valid_colors)
        pos = rd.randrange(0, len(new_chrom))
        new_chrom = new_chrom[0:pos] + [new_gene] + new_chrom[pos+1:]
        return new_chrom
        
   
if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem()
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    print(
        f"Best guess {solver.get_best_individual().chromosome}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
