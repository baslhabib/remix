# genetic_algorithm.py

import random

def fitness(individual):
    # Define a fitness function
    return sum(individual)

def select(population):
    # Select two parents
    return random.choices(population, k=2)

def crossover(parent1, parent2):
    # Crossover logic
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    # Mutate the individual
    index = random.randint(0, len(individual) - 1)
    individual[index] = random.randint(0, 1)

def genetic_algorithm(population_size, generations):
    population = [[random.randint(0, 1) for _ in range(5)] for _ in range(population_size)]
    
    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        next_generation = population[:2]  # Elitism, keep the best individuals
        
        while len(next_generation) < population_size:
            parent1, parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_generation += [child1, child2]
        
        population = next_generation
        
    return sorted(population, key=fitness, reverse=True)

if __name__ == "__main__":
    best_solution = genetic_algorithm(population_size=10, generations=20)
    print("Best Solution:", best_solution[0])
