import random


##########################################################
##        Retorna true si el valor es un entero         ##
##########################################################
bandera_linux = 1
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


# Function that adds the individual to a generation and calculates fitness
def agregar_individuo(hijo, nuevo_viejo):
    if (nuevo_viejo == 0):
        poblacion.append(hijo)
        fitness.append(verificar(hijo))

    else:
        descendientes.append(hijo)
        fitness_nuevo.append(verificar(hijo))


# Function that generate the poblacion, also evaluates it
def generar_poblacion():
    for i in range(tamano_poblacion):
        individuo = []
        for j in range(tamano_tablero):
            individuo.append(random.randint(0, tamano_tablero - 1))
        agregar_individuo(individuo, 0)


# Function that returns the total of collisions of an individual
def verificar(individuo):
    colisiones = 0
    for i in range(tamano_tablero): #verifica colisiones en la fila
        if i not in individuo:
            colisiones += 1

    # Verifica colisiones en diagonal
    for i in range(0, tamano_tablero - 1):

        # Derecha arriba
        for j, k in zip(range(individuo[i] - 1, -1, -1), range(i + 1, tamano_tablero)):
            if individuo[k] == j:
                colisiones += 1
                break

        # Derecha abajo
        for j, k in zip(range(individuo[i] + 1, tamano_tablero), range(i + 1, tamano_tablero)):
            if individuo[k] == j:
                colisiones += 1
                break

    return colisiones


# Function that mutate child
def mutar_hijo(hijo):
    for i in range(len(hijo)):
        mutacion_random = random.randint(0, 100) / 100
        if (mutacion_random < porcentaje_mutacion):
            hijo[random.randint(0, tamano_tablero - 1)] = random.randint(0, tamano_tablero - 1)  # cambiar gen
    agregar_individuo(hijo, 1)


# Function that represents the process of selection, which
def seleccion():
    seleccion_random = random.sample(list(enumerate(fitness)), cant_seleccionada)

    mejor_fitness = min(seleccion_random, key=lambda t: t[1])  #tupla = (index, fitness)

    mejor_individuo = poblacion[mejor_fitness[0]]
    return mejor_individuo


def elitismo():
    lista_indice_fitness = list(enumerate(fitness))
    mejor = sorted(lista_indice_fitness, key=lambda t: t[1])
    mejor = mejor[:cant_seleccionada]
    for i in mejor:
        agregar_individuo(poblacion[i[0]], 1)


# Function that combines the father and the mother, returns two childs
def crossover(padre, padre2):
    pos = random.randint(1, 6)
    hijo1 = padre[:pos] + padre2[pos:]
    hijo2 = padre2[:pos] + padre[pos:]
    # return (hijo1, hijo2)
    mutar_hijo(hijo1)
    mutar_hijo(hijo2)


def crear_poblacion():
    global poblacion
    global descendientes
    global fitness
    global fitness_nuevo
    if (eliticismo == 1):
        for i in range(int((tamano_poblacion - cant_seleccionada) / 2)):
            mejor1 = seleccion()
            mejor2 = seleccion()
            crossover(mejor1, mejor2)
        elitismo()
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
        for j in range(tamano_solucion):
            if (i != solucion[j]):
                fila.append(0)
            else:
                fila.append(1)
        matriz.append(fila)
    return matriz


def imprimir(solucion):
    matriz_solucion = get_solucion(solucion)
    matriz_cont = 0

    for i in range(tamano_tablero * 2 + 1):
        if (i == 0):
            print("  " + " - ".join("+" for i in range(tamano_tablero + 1)))
        elif (i % 2 != 0):
            respuesta = " " + " |"
            fila = matriz_solucion[matriz_cont]
            for j in range(len(solucion)):
                respuesta += " "
                if (fila[j] == 0 and (matriz_cont + j) % 2 == 1): respuesta
                if (fila[j] == 1): respuesta
                respuesta += str(fila[j]) + " |"
            respuesta += "  " + str(matriz_cont + 1)
            matriz_cont += 1
            print(respuesta)
        elif (i % 2 == 0):
            print("  " + " - ".join("+" for i in range(tamano_tablero + 1)))


def es_entero(num):
    try:
        int(num)
        return True

    except ValueError:
        return False


def elegir_opcion():
    opcion = input("Elegir opcion: ")
    if es_entero(opcion):
        opcion = int(opcion)
        if 0 < opcion < 3:
            return opcion

    input("Valor incorrecto, presione ENTER para volver")
    opcion = elegir_opcion()
    return opcion


def modificar_tamano_tablero():
    global tamano_tablero
    tam_tab = input("Seleccione tamano del tablero (minimo 4): ")
    if es_entero(tam_tab):
        tam_tab = int(tam_tab)
        if tam_tab >= 4:
            tamano_tablero = tam_tab
        else:
            input("Tablero debe ser mas grande, presione ENTER para volver")
            modificar_tamano_tablero()
    else:
        input("Valor incorrecto, presione ENTER para volver")
        modificar_tamano_tablero()


def modificar_tamano_poblacion():
    global tamano_poblacion
    global cant_seleccionada

    tam_p = input("Seleccione tamano de poblacion (minimo 50): ")
    if es_entero(tam_p):
        tam_p = int(tam_p)
        if tam_p >= 50:
            tamano_poblacion = tam_p
            cant_seleccionada = int(tamano_poblacion * 0.1)
        else:
            input("Poblacion deberia ser mas grande, presione ENTER para volver")
            modificar_tamano_poblacion()
    else:
        input("Valor incorrecto, presione ENTER para volver")
        modificar_tamano_poblacion()


def modificar_porcentaje_mutacion():
    global porcentaje_mutacion
    porcent_mut = input("Seleccione porcentaje de mutacion (1-5): ")
    if es_entero(porcent_mut):
        porcent_mut = int(porcent_mut)
        if 1 <= porcent_mut <= 5:
            porcentaje_mutacion = porcent_mut / 100
        else:
            input("Valor fuera de rango, presione ENTER para volver")
            modificar_porcentaje_mutacion()
    else:
        input("Valor incorrecto, presione ENTER para volver")
        modificar_porcentaje_mutacion()


def modificar_limite_genes():
    global limite_genes
    tam_g = input("Ingrese limite de generaciones (minimum 50): ")
    if es_entero(tam_g):
        tam_g = int(tam_g)
        if tam_g >= 50:
            limite_genes = tam_g
        else:
            input("Fuera de rango, presione ENTER para volver")
            modificar_limite_genes()
    else:
        input("Valor incorrecto, presione ENTER para volver")
        modificar_limite_genes()


def modificar_eliticismo():
    global eliticismo
    val_e = input("Eliticismo? 1)si 0)no: ")
    if es_entero(val_e):
        val_e = int(val_e)
        if val_e == 0 or val_e == 1:
            eliticismo = val_e
    else:
        input("Valor incorrecto, presione ENTER para volver")
        modificar_eliticismo()


def impresion_pasos():
    opcion = input("Desea imprimir paso a paso? 1)si 0)no: ")
    if es_entero(opcion):
        opcion = int(opcion)
        if 0 <= opcion < 2:
            return opcion

    input("Valor incorrecto, presione ENTER para volver")
    opcion = elegir_opcion()
    return opcion


def main():
    solucion = 0
    print("#####################################################")
    print("## Problema de N-Reinas con algoritmos genéticos ####")
    print("#####################################################")
    print("Para comenzar, seleccione los valores\n")
    print("\n 1.Valores por Defecto:\n\t-Tamano tablero: 8 \n\t-Poblacion: 100 individuos\n\t-Generaciones: 500",
          "\n\t-Porcentaje mutacion: 2% \n\t-Elitismo: No aplica")
    print("\n 2.Valores Personalizados\n")
    option = elegir_opcion()

    if option == 2:
        modificar_tamano_tablero()
        modificar_tamano_poblacion()
        modificar_limite_genes()
        modificar_porcentaje_mutacion()
        modificar_eliticismo()

    bandera_pasos = impresion_pasos()
    generar_poblacion()

    for i in range(limite_genes):
        crear_poblacion()

        if bandera_pasos:
            mejor_fitness = min(fitness)
            indice = fitness.index(mejor_fitness)
            mejor_gen = poblacion[indice]
            print("\nGeneracion: " + str(i))
            print("  Mejor generacion " + str(poblacion[indice]) + "--> fitness: " + str(mejor_fitness))
        if 0 in fitness:
            print("\nSOLUCION encontrada.")
            print("Numero de generaciones realizadas: " + str(i) + " of " + str(limite_genes))
            indice = fitness.index(0)
            print("Respuesta Corta: " + str(poblacion[indice]))
            print("\nRespuesta Larga: \n1: Reinas\n0: Espacio en blanco")
            imprimir(poblacion[indice])
            solucion = 1
            break
    if (solucion == 0):
        print("No hubo ninguna solucion.")
        # print("Number of individuals: " + str(tamano_poblacion))
        # print("Number of generations executed: " + str(limite_genes))
        # print("Mutation percent: " + str(porcentaje_mutacion))


if __name__ == "__main__":
    main()

