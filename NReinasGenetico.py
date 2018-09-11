##########################################################
## Esta funcion retorna true si el valor es un entero   ##
##########################################################
def es_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

 
#################################################
## Esta funcion modifica el tamaño del tablero ##
#################################################
def modificar_tamano_tablero():
    global tamano_tablero
    b_tamano = input("Ingrese el tamaño del tablero: ")
    if es_int(b_tamano):
        if int(b_tamano) > 3:
            tamano_tablero = int(b_tamano)
        else:
            input("El número debe ser mayor o igual a 4, precione ENTER para continuar")
            modificar_tamano_tablero()
    else:
        input("Valor incorrecto, precione ENTER para continuar")
        modificar_tamano_tablero()


#####################################################
## Esta funcion modifica el tamaño de la población ##
#####################################################
def modificar_tamano_poblacion():
    global cantidad_seleccionada
    global tamano_poblacion
    b_tamano = input("Ingrese el tamaño de la población: ")
    if es_int(b_tamano):
        b_tamano = int(b_tamano)
        if b_tamano >= 50:
            tamano_poblacion = b_tamano
            cantidad_seleccionada = int(tamano_poblacion * 0.1)
        else:
            input("El número debe ser mayor o igual a 50, precione ENTER para continuar")
            modificar_tamano_poblacion()
    else:
        input("Valor incorrecto, precione ENTER para continuar")
        modificar_tamano_poblacion()
            




def modificar_porcentaje_mutacion():
    global mutation_percent    
    m_size = input("Enter mutation percent (1-5): ")
    if is_int(m_size):
        m_size = int(m_size)
        if 1 <= m_size <= 5:
            mutation_percent = m_size/100
        else:
            input("Outside the range of allowed values, precione ENTER para continuar")
            modify_mutation_percent()
    else:
        input("Valor incorrecto, precione ENTER para continuar")
        modify_mutation_percent()


def modificar_limite_genes():
    global limit_gens
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


def modificar_elitisto():
    global eliticism
    e_value = input("Elitism? (yes:1 no:0): ")
    if is_int(e_value):
        e_value = int(e_value)
        if e_value == 0 or e_value == 1:
            eliticism = e_value
    else:
        input("Incorrect value, press ENTER to go back")
        modify_elitism()

        
def seleccionar_opciones():
    opcion_seleccionada = input("Choose option: ")
    try:
        opcion_seleccionada = int(opcion_seleccionada)
        if 0 < option < 3:
            return option
    except ValueError:
        input("Datos invalidos, precione ENTER para continuar")
        return seleccionar_opciones()


     
    
    
     

def main():
    solution = 0
    print("\nProblema de N-Reinas con algoritmos genéticos\n")
    print("To start the program choose the types of values to use\n")
    print("\n 1.Default values(*)\n 2.Custom values")
    print("\n(*)Default values: \n\t-Board size: 8 \n\t-Population: 100 individuals\n\t-Generations: 500",
    	"\n\t-Percent mutation: 2% \n\t-Elitism:No apply\n")
    
    modificar_tamano_tablero()
    modificar_tamano_poblacion()
    modificar_limite_genes()
    modificar_porcentaje_mutacion()
    modificar_elitisto()
    
    #steps_flag = choose_step_print()
    #generate_population()
    #for i in range(limit_gens): 
    #    create_new_population()
    #    if steps_flag:
    #        best_fitness = min(fitness)
    #        index = fitness.index(best_fitness)
    #        best_gen = population[index] 
    #        print("\nGeneration: "+ str(i))
    #        print("  Best gen: " + str(population[index]) + ", fitness: " + str(best_fitness))
    #    if 0 in fitness:
    #        print("\nThere IS a solution in the population. \nStats:")
    #        #print("Number of individuals: " + str(population_size))
    #        print("Number of generations executed: " + str(i) + " of " + str(limit_gens))
    #        #print("Mutation percent: " + str(mutation_percent))
    #        index = fitness.index(0)
    #        print("Short answer: " + str(population[index]))
    #        print("\nLong answer: \n1: queens\n0: blank space")
    #        print_solution(population[index])
    #        solution = 1
    #        break
    #if(solution == 0): 
    #    print("There was no solution in the final population.")
        #print("Number of individuals: " + str(population_size))
        #print("Number of generations executed: " + str(limit_gens))
        #print("Mutation percent: " + str(mutation_percent))


if __name__ == "__main__":
    main()
    
