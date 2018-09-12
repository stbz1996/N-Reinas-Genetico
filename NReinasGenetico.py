import random

bandera = 1
tamano_tablero = 8
tamano_poblacion = 100
porcentaje_mutacion = 0.02
limite_genes = 500
eliticismo = 0
poblacion = []
descendientes = []
fitness = []
fitness_nuevo = []
cant_selected = int(tamano_poblacion * 0.1)


##########################################################
##        Retorna true si el valor es un entero         ##
##########################################################
def es_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

#################################################
##      Modifica el tamaño del tablero         ##
#################################################
def verificar(individual):
    colisiones = 0
    # Verifica colisiones en la fila
    for i in range(tamano_tablero):
        if i not in individual:
            colisiones += 1

    # Verifica colisiones en las diagonales
    for i in range(0, tamano_tablero - 1):

        # Verifica derecha arriba
        for j, k in zip(range(individual[i] - 1, -1, -1), range(i + 1, tamano_tablero)):
            if individual[k] == j:
                colisiones += 1
                break

        # Verifica derecha abajo
        for j, k in zip(range(individual[i] + 1, tamano_tablero), range(i + 1, tamano_tablero)):
            if individual[k] == j:
                colisiones += 1
                break

    return colisiones


#################################################
##      Modifica el tamaño del tablero         ##
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
##        Modifica el tamaño de la población       ##
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
##         Modifica el % de la mutación            ##
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
##         Modifica el limite de genes             ##
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
    if (nuevo_o_viejo == 0):
        poblacion.append(hijo)
        fitness.append(verificar(hijo))
    else:
        descendientes.append(hijo)
        fitness_nuevo.append(verificar(hijo))  ## Falta esta funcion de traducir


#####################################################
##         Función que muta al hijo                ##
#####################################################
def mutar(hijo):
    for i in range(len(hijo)):
        mutacion_aleatoria = random.randint(0, 100) / 100
        if (mutacion_aleatoria < porcentaje_mutacion):
            hijo[random.randint(0, tamano_tablero - 1)] = random.randint(0, tamano_tablero - 1)  # cambia aleatoriamente un gen
    agregar_individual(hijo, 1)

#####################################################
##       Proceso de seleccion de la poblacion      ##
#####################################################
# Function that represents the process of selection, which
def seleccion():
    seleccion_aleatoria = random.sample(list(enumerate(fitness)), cant_selected)

    mejor_fitness = min(seleccion_aleatoria, key=lambda t: t[1])  # tupla = (index, fitness)

    mejor_individuo = poblacion[mejor_fitness[0]]
    return mejor_individuo


def seleccionar_elite():
    lista_indices_fitness = list(enumerate(fitness))
    mejor = sorted(lista_indices_fitness, key=lambda t: t[1])
    mejor = mejor[:cant_selected]
    for i in mejor:
        agregar_individual(poblacion[i[0]], 1)

#####################################################
##      Combina los padres y retorna 2 hijos       ##
#####################################################
def crossover(padre, madre):
    pos = random.randint(1, 6)
    hijo1 = padre[:pos] + madre[pos:]
    hijo2 = madre[:pos] + padre[pos:]

    mutar(hijo1)
    mutar(hijo2)


def crear_nueva_poblacion():
    global poblacion
    global descendientes
    global fitness
    global fitness_nuevo
    if (eliticismo == 1):
        for i in range(int((tamano_poblacion - cant_selected) / 2)):
            mejor1 = seleccion()
            mejor2 = seleccion()
            crossover(mejor1, mejor2)
        seleccionar_elite()
    else:
        for i in range(int(tamano_poblacion / 2)):
            mejor1 = seleccion()
            mejor2 = seleccion()
            crossover(mejor1, mejor2)
    poblacion = descendientes
    fitness = fitness_nuevo
    descendientes = []
    fitness_nuevo = []


def get_solucion(solucion):
    matriz = []
    tamano_solucion = len(solucion)
    for i in range(tamano_solucion):
        fila = []
        for j in range(tamano_solucion):  # row
            if (i != solucion[j]):
                fila.append(0)
            else:
                fila.append(1)
        matriz.append(fila)
    return matriz


def generar_poblacion():
    for i in range(tamano_poblacion):
        individual = []
        for j in range(tamano_tablero):
            individual.append(random.randint(0, tamano_tablero - 1))
        agregar_individual(individual, 0)


def imprimir_solucion(solucion):
    matriz_solucion = get_solucion(solucion)
    matriz_cont = 0

    # Condition if program running in Windows OS
    if not bandera:
        bcolors.RED = ""
        bcolors.WHITE = ""
        bcolors.GREEN = ""
        bcolors.BLACK = ""

    for i in range(tamano_tablero * 2 + 1):
        if (i == 0):
            print(bcolors.RED + "  " + " - ".join("+" for i in range(tamano_tablero + 1)) + bcolors.WHITE)
        elif (i % 2 != 0):
            respuesta = " " + bcolors.RED + " |" + bcolors.WHITE
            fila = matriz_solucion[matriz_cont]
            for j in range(len(solucion)):
                respuesta += " "
                if (fila[j] == 0 and (matriz_cont + j) % 2 == 1): respuesta += bcolors.BLACK
                if (fila[j] == 1): respuesta += bcolors.GREEN
                respuesta += str(fila[j]) + bcolors.RED + " |" + bcolors.WHITE
            respuesta += "  " + str(matriz_cont)
            matriz_cont += 1
            print(respuesta)
        elif (i % 2 == 0):
            print(bcolors.RED + "  " + " - ".join("+" for i in range(tamano_tablero + 1)) + bcolors.WHITE)


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
    # for i in range(limite_genes):
    #    crear_nueva_poblacion()
    #    if steps_flag:
    #        best_fitness = min(fitness)
    #        index = fitness.index(best_fitness)
    #        best_gen = population[index]
    #        print("\nGeneration: "+ str(i))
    #        print("  Best gen: " + str(population[index]) + ", fitness: " + str(best_fitness))
    #    if 0 in fitness:
    #        print("\nThere IS a solution in the population. \nStats:")
    #        #print("Number of individuals: " + str(population_size))
    #        print("Number of generations executed: " + str(i) + " of " + str(limite_genes))
    #        #print("Mutation percent: " + str(porcentaje_mutacion))
    #        index = fitness.index(0)
    #        print("Short answer: " + str(population[index]))
    #        print("\nLong answer: \n1: queens\n0: blank space")
    #        imprimir_solucion(population[index])
    #        solution = 1
    #        break
    # if(solution == 0):
    #    print("There was no solution in the final population.")
    # print("Number of individuals: " + str(population_size))
    # print("Number of generations executed: " + str(limite_genes))
    # print("Mutation percent: " + str(porcentaje_mutacion))


if __name__ == "__main__":
    main()

