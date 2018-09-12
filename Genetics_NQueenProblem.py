import random

linux_flag = 1
tamano_tablero = 8
tamano_poblacion = 100
porcentaje_mutacion = 0.02
limite_genes = 500
eliticismo = 0
poblacion = []
descendientes = []
fitness = []
fitness_nuevo = []
cant_seleccionada = int(tamano_poblacion * 0.1)


#Function that adds the individual to a generation and calculates fitness
def add_individual(child, new_or_old): 
    
    #new is 1, old is 0 
    if (new_or_old==0): 
        poblacion.append(child)
        fitness.append(check(child))
        
    else: 
        descendientes.append(child)
        fitness_nuevo.append(check(child))
        


#Function that generate the poblacion, also evaluates it
def generate_population(): 
    for i in range(tamano_poblacion):
        #generates only one
        individual = []
        for j in range(tamano_tablero):
            #adding the genes
            individual.append(random.randint(0, tamano_tablero - 1))
        #add to the poblacion or group
        #adds the fitness to the fitness array that corresponds to poblacion too.
        add_individual(individual, 0)
        


#Function that returns the total of collisions of an individual
def check(individual):
    collisions = 0
    #Check collisions in row
    for i in range(tamano_tablero):
        if i not in individual:
            collisions += 1

    #Check collisions in diagonals
    for i in range(0, tamano_tablero - 1):
    
        #Check right upper
        for j, k in zip(range(individual[i]-1,-1,-1), range(i+1, tamano_tablero)):
            if individual[k] == j:
                collisions += 1
                break
                
        #Check right lower
        for j, k in zip(range(individual[i]+1, tamano_tablero), range(i + 1, tamano_tablero)):
            if individual[k] == j:
                collisions += 1
                break
                
    return collisions




#Function that mutate child 
def mutate_after_creation(child): 
    for i in range(len(child)): 
        random_mutate = random.randint(0,100) / 100
        if (random_mutate < porcentaje_mutacion):
            child[random.randint(0, tamano_tablero - 1)] = random.randint(0, tamano_tablero - 1) #change a random gen
    add_individual(child, 1)



#Function that represents the process of selection, which 
def tournament_selection():
    random_selection = random.sample(list(enumerate(fitness)), cant_seleccionada)
    #print(random_selection)
    best_fitness = min(random_selection, key = lambda t: t[1]) #minimun fitness on the sample, tuple = (index, fitness)
    #print(best_fitness)
    best_individual = poblacion[best_fitness[0]]
    return best_individual


def elitism():
    list_index_fitness = list(enumerate(fitness))
    best = sorted(list_index_fitness, key = lambda t: t[1])
    best = best[:cant_seleccionada]
    for i in best:
        add_individual(poblacion[i[0]], 1)
    
    
    

#Function that combines the father and the mother, returns two childs 
def crossover(father, mother):
    pos = random.randint(1,6)
    child_one = father[:pos]+mother[pos:]
    child_two = mother[:pos]+father[pos:]
    #return (child_one, child_two)
    mutate_after_creation(child_one)
    mutate_after_creation(child_two)

def create_new_population(): 
    global poblacion
    global descendientes
    global fitness
    global fitness_nuevo
    if (eliticismo == 1):
        for i in range(int((tamano_poblacion - cant_seleccionada) / 2)):
            best_1 = tournament_selection()
            best_2 = tournament_selection()
            crossover(best_1,best_2)
        elitism()
    else: 
        for i in range(int(tamano_poblacion / 2)):
            best_1 = tournament_selection()
            best_2 = tournament_selection()
            crossover(best_1,best_2)
    population = offsprings
    fitness = fitness_new
    offsprings = [] 
    fitness_new = [] 
    
    
   
def get_matrix_solution(solution): 
    matrix = []
    len_sol = len(solution)
    for i in range(len_sol): 
        row = []
        for j in range(len_sol): #row
            if (i != solution[j]):
                row.append(0)
            else: 
                row.append(1)
        matrix.append(row)
    return matrix

    
def print_solution(solution):
    matrix_solution = get_matrix_solution(solution)
    matrix_cont = 0
    	
    for i in range(tamano_tablero * 2 + 1): #para futuro deberia ser solution * 2 - 1
        if (i == 0):
            print("  " + " - ".join("+" for i in range(tamano_tablero + 1)))
        elif (i%2 != 0):
            answer = " " + " |"
            row = matrix_solution[matrix_cont]
            for j in range(len(solution)):
                answer += " "
                if(row[j] == 0 and (matrix_cont+j) %2 == 1): answer
                if(row[j] == 1):answer
                answer += str(row[j]) + " |"
            answer += "  " + str(matrix_cont)
            matrix_cont += 1 
            print(answer)
        elif (i%2 == 0):
            print("  " + " - ".join("+" for i in range(tamano_tablero + 1)))

             
def is_int(number):
    try:
        int(number)
        return True
    
    except ValueError:
        return False


def choose_option():
    option = input("Choose option: ")
    if is_int(option):
        option = int(option)
        if 0 < option < 3:
            return option
            
    input("Incorrect value, press ENTER to go back")
    option = choose_option()
    return option


def modify_board_size():
    global tamano_tablero
    b_size = input("Enter board size (minimum 4): ")
    if is_int(b_size):
        b_size = int(b_size)
        if b_size >= 4:
            board_size = b_size
        else:
            input("Board should be bigger, press ENTER to go back")
            modify_board_size()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_board_size()


def modify_population_size():
    global tamano_poblacion
    global cant_seleccionada #int(tamano_poblacion * 0.1)
    
    p_size = input("Enter poblacion size (minimum 50): ")
    if is_int(p_size):
        p_size = int(p_size)
        if p_size >= 50:
            population_size = p_size
            cant_selected = int(population_size * 0.1)
        else:
            input("Population should be bigger, press ENTER to go back")
            modify_population_size()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_population_size()
            

def modify_mutation_percent():
    global porcentaje_mutacion
    m_size = input("Enter mutation percent (1-5): ")
    if is_int(m_size):
        m_size = int(m_size)
        if 1 <= m_size <= 5:
            mutation_percent = m_size/100
        else:
            input("Outside the range of allowed values, press ENTER to go back")
            modify_mutation_percent()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_mutation_percent()


def modify_limit_gens():
    global limite_genes
    g_size = input("Enter generations limit (minimum 50): ")
    if is_int(g_size):
        g_size = int(g_size)
        if g_size >= 50:
            limit_gens = g_size
        else:
            input("Outside the range of allowed values, press ENTER to go back")
            modify_limit_gens()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_limit_gens()


def modify_elitism():
    global eliticismo
    e_value = input("Elitism? (yes:1 no:0): ")
    if is_int(e_value):
        e_value = int(e_value)
        if e_value == 0 or e_value == 1:
            eliticism = e_value
    else:
        input("Incorrect value, press ENTER to go back")
        modify_elitism()


def choose_step_print():
    option = input("Want to print step by step? (yes:1 no:0): ")
    if is_int(option):
        option = int(option)
        if 0 <= option < 2:
            return option
            
    input("Incorrect value, press ENTER to go back")
    option = choose_option()
    return option






            
def main():
    solution = 0
    print("#####################################################")
    print("## Problema de N-Reinas con algoritmos genéticos ####")
    print("#####################################################")
    print("To start the program choose the types of values to use\n")
    print("\n 1.Default values(*)\n 2.Custom values")
    print("\n(*)Default values: \n\t-Board size: 8 \n\t-Population: 100 individuals\n\t-Generations: 500",
    	"\n\t-Percent mutation: 2% \n\t-Elitism:No apply\n")
    option = choose_option()
    
    if option == 2:
        modify_board_size()
        modify_population_size()
        modify_limit_gens()
        modify_mutation_percent()
        modify_elitism()
    
    steps_flag = choose_step_print()
    generate_population()
    for i in range(limite_genes):
        create_new_population()
        if steps_flag:
            best_fitness = min(fitness)
            index = fitness.index(best_fitness)
            best_gen = poblacion[index]
            print("\nGeneration: "+ str(i))
            print("  Best gen: " + str(poblacion[index]) + ", fitness: " + str(best_fitness))
        if 0 in fitness:
            print("\nThere IS a solution in the poblacion.")
            print("Number of generations executed: " + str(i) + " of " + str(limite_genes))
            index = fitness.index(0)
            print("Short answer: " + str(poblacion[index]))
            print("\nLong answer: \n1: queens\n0: blank space")
            print_solution(poblacion[index])
            solution = 1
            break
    if(solution == 0): 
        print("There was no solution in the final poblacion.")
        #print("Number of individuals: " + str(tamano_poblacion))
        #print("Number of generations executed: " + str(limite_genes))
        #print("Mutation percent: " + str(porcentaje_mutacion))


if __name__ == "__main__":
    main()
    
