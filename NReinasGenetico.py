import random

linux_flag = 1
tamano_tablero = 8
tamano_poblacion = 100
mutation_percent = 0.02
limit_gens = 500
eliticism = 0
poblacion = []
descendientes = []
fitness = []
fitness_new = []
cant_selected = int(tamano_poblacion * 0.1)

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
            



#####################################################
## Esta funcion modifica el % de la mutación       ##
#####################################################
def modificar_porcentaje_mutacion():
    global porcentaje_mutacion    
    m_tamano = input("Ingrese el % de mutación, entre 1 y 5: ")
    if es_int(m_tamano):
        m_tamano = int(m_tamano)
        if 1 <= m_tamano <= 5:
            porcentaje_mutacion = m_tamano / 100
        else:
            input("El número debe estar entre 1 y 5, precione ENTER para continuar")
            modificar_porcentaje_mutacion()
    else:
        input("Valor incorrecto, precione ENTER para continuar")
        modificar_porcentaje_mutacion()


#####################################################
## Esta funcion modifica el limite de genes        ##
#####################################################
def modificar_limite_genes():
    global limite_genes
    g_tamano = input("Ingrese el límite de generaciones (Al menos 50): ")
    if es_int(g_tamano):
        g_tamano = int(g_tamano)
        if g_tamano >= 50:
            limite_genes = g_tamano
        else:
            input("El número debe ser mayor o igual a 50, precione ENTER para continuar")
            modificar_limite_genes()
    else:
        input("Valor incorrecto, precione ENTER para continuar")
        modificar_limite_genes()
        


def agregar_individual(hijo, nuevo_o_viejo): 
    if (nuevo_o_viejo==0): 
        poblacion.append(hijo)
        fitness.append(check(hijo))    
    else: 
        descendientes.append(hijo)
        fitness_new.append(check(hijo)) ## Falta esta funcion de traducir 


def generar_poblacion(): 
    for i in range(tamano_poblacion):
        individual = []
        for j in range(tamano_tablero):
            individual.append(random.randint(0,tamano_tablero-1))
        agregar_individual(individual, 0)

     
    
    


def main():
    solution = 0
    print("#####################################################")
    print("## Problema de N-Reinas con algoritmos genéticos ####")
    print("#####################################################")

    modificar_tamano_tablero()
    modificar_tamano_poblacion()
    modificar_limite_genes()
    modificar_porcentaje_mutacion()
    

    generar_poblacion()
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
    
