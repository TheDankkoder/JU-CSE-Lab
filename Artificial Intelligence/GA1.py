import random

# Define the multivariable function to maximize
C =[[4,4,4,4],[1,1,1,1],[8,8,8,8],[6,6,6,6],[3,7,3,7],[2,9,2,9],[5,3,5,3],[8,1,8,1],[6,2,6,2],[7,3.6,7,3.6]]

B = [1,2,2,4,4,6,3,7,5,5]
myInt = 10

B[:] = [x / myInt for x in B]

def f(x1, x2, x3, x4):
    return - ((x1 - 5)**2 + (x2 - 3)**2 + (x3 - 2)**2 + (x4 - 7)**2)**(-1)

# Define the chromosome length and bounds for each variable
num_vars = 4
bits_per_var = 4
chromosome_length = num_vars * bits_per_var
bounds = [(0, 10)] * num_vars

# Define the fitness function
def fitness(chromosome):
    vars = []
    for i in range(num_vars):
        start = i * bits_per_var
        end = start + bits_per_var
        var = int(chromosome[start:end], 2)
        var = bounds[i][0] + var * (bounds[i][1] - bounds[i][0]) / (2**bits_per_var - 1)
        vars.append(var)
    return f(*vars)

# Define the tournament selection function
def tournament_selection(population, size):
    tournament = random.sample(population, size)
    winner = max(tournament, key=lambda x: fitness(x))
    return winner

# Define the single-point crossover operator
def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Define the mutation operator
def bit_flip_mutation(chromosome, mutation_probability):
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < mutation_probability:
            # Flip the bit
            mutated_bit = "0" if bit == "1" else "1"
        else:
            mutated_bit = bit
        mutated_chromosome += mutated_bit
    return mutated_chromosome

# Initialize the population
population_size = 20
population = []
for i in range(population_size):
    chromosome = ""
    for j in range(chromosome_length):
        bit = str(random.randint(0, 1))
        chromosome += bit
    population.append(chromosome)

# Evolution loop
num_generations = 500
tournament_size = 2
crossover_probability = 0.5
mutation_probability = 0.1

for generation in range(num_generations):
    # Select parents for crossover
    parents = []
    for i in range(population_size):
        parent1 = tournament_selection(population, tournament_size)
        parent2 = tournament_selection(population, tournament_size)
        parents.append((parent1, parent2))

    # Perform crossover and mutation to create new offspring
    offspring = []
    for parent1, parent2 in parents:
        if random.random() < crossover_probability:
            child1, child2 = single_point_crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        child1 = bit_flip_mutation(child1, mutation_probability)
        child2 = bit_flip_mutation(child2, mutation_probability)
        offspring.extend([child1, child2])

    # Evaluate fitness of offspring and select the next generation
    population = sorted(offspring, key=lambda x: fitness(x), reverse=True)[:population_size]

    # Print the best fitness value in each generation
    print(f"Generation {generation+1}: Best Fitness = {fitness(population[0])}")

# Print the best solution
best_chromosome = population[0]
best_vars = []
for i in range(num_vars):
    start = i * bits_per_var
    end = start + bits_per_var
    var = int(best_chromosome[start:end], 2)
    var = bounds[i][0] + var * (bounds[i][1] - bounds[i][0]) / (2**bits_per_var - 1)
    best_vars.append(var)
best_fitness = f(*best_vars)
print("Best Solution:")
print(f"  Variables: {best_vars}")
print(f"  Fitness: {best_fitness}")