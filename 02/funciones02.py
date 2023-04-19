#0
def stark_normalizar_datos(lista:list):
    """
    Recibe una lista
    Normaliza los datos
    Valida que no sea el del tipo al cual sera casteado
    si un dato fue modificado imprime: Datos normalizados
    y valida que no este vacia
    Retorna los datos casteados
    """ 
    if len(lista) > 0:
        for dato in lista:
            if type(dato["altura"]) != type(float()):
                dato["altura"] = float(dato["altura"])
            if type(dato["peso"]) != type(float()):
                dato["peso"] = float(dato["peso"])
        if (type(dato["peso"]) and type(dato["altura"])) == type(float()):
            print("Datos normalizados")
    else:
        print("Error: Lista de heroes vacía")

#1.1
def obtener_nombre(heroe:dict) -> str:
    """
    Recibe un diccionario
    y retorna un string con el nombre del superheroe reformateado
    asi: Nombre: Howard the duck
    """
    nombre = "Nombre: {0}".format(heroe["nombre"])
    return nombre

#1.2
def imprimir_dato(dato:str):
    """
    Recibe un dato 
    y lo imprime
    """
    print(dato)

#1.3
def stark_imprimir_nombres_heroes(lista:list):
    """
    Recibe una lista
    verifica que la lista tenga elementos
    y por cada elemento en la lista formatea el nombre y lo imprime en la consola
    y si no tiene elementos retorna -1
    """
    retorno = -1
    if len(lista) > 0:
        for heroe in lista:
            nombre = obtener_nombre(heroe)
            retorno = imprimir_dato(nombre)
        return retorno
    else:
        return retorno

#2
def obtener_nombre_y_dato(heroe:dict, clave:str) -> str:
    """
    recibe un diccionario y una clave que representa lo que se desea obtener
    Devuelve un string con el nombre y el dato del heroe reformateado
    """
    retorno = "Nombre: {0} | {1} {2}".format(heroe["nombre"], clave, round(heroe[clave],2))
    return retorno

#3
def stark_imprimir_nombres_alturas(lista:list):
    """
    Recibe una lista y itera a traves de ella
    y imprime sus nombres y alturas utilizando la funcion creada anteriormente
    y valida que la lista no este vacia si es asi retorna -1
    """
    retorno = -1
    if len(lista) > 0:
        for heroe in lista:
            nombre = obtener_nombre_y_dato(heroe, "altura")
            retorno = print(nombre)
        return retorno
    else:
        return retorno

#4.1
def calcular_max(lista:list, clave:str) -> int:
    """
    Recibe una lista tipo list y una clave tipo str
    Y calcula el maximo de la clave dada en la lista
    Y retorna el maximo en entero
    """
    maximo = lista[0]
    for heroe in lista:
        if maximo[clave] < heroe[clave]:
            maximo = heroe
    return maximo

#4.2
def calcular_min(lista:list, clave:str) -> dict:
    """
    Recibe una lista tipo list y una clave tipo str
    Y calcula el minimo de la clave dada en la lista
    Y retorna el minimo en entero
    """
    minimo = lista[0]
    for heroe in lista:
        if minimo[clave] > heroe[clave]:
            minimo = heroe
    return minimo

#4.3
def calcular_max_min_dato(lista:list, estado:str, clave:str) -> dict:
    """
    Recibe una lista tipo list, un estado tipo str que puede ser max o min, y una clave tipo str (altura, peso, etc)
    Utiliza las funciones calcular_min o calcular_max segun
    y retorna un entero que seria el maximo o minimo segun
    """
    if estado == "max":
        maxmin = calcular_max(lista, clave)
    elif estado == "min":
        maxmin = calcular_min(lista, clave)
    elif estado != "max" and estado != "min":  
        return -1
    return maxmin

#4.4
def stark_calcular_imprimir_heroe(lista:list, estado:str, clave:str) -> str:
    """
    Recibe una lista tipo list, un estado tipo str que puede ser max o min, y una clave tipo str (altura, peso, etc)
    a traves de la funcion calcular_max_min_dato calcula el max o min en la lista segun la clave
    y lo imprime como un dato str formateado ejemplo(Max Altura: Nombre: Groot | altura 701)
    """
    superheroe = calcular_max_min_dato(lista, estado, clave)
    retorno = obtener_nombre_y_dato(superheroe, clave)
    retorno = "{0} {1}: {2}".format(estado, clave, retorno)
    imprimir_dato(retorno)

#5.1
def sumar_dato_heroe(lista:list, clave:str) -> float:
    """
    Recibe una lista tipo list, y una clave tipo string
    Valida que cada heroe sea un diccionario y que no sea un dict vacio y suma todos todos los heroes segun la clave
    Retorna la suma de todos los datos segun la clave
    """
    acu_datos = 0
    for heroe in lista:
        if len(heroe) > 0 and type(heroe) == type(dict()):
            acu_datos += heroe[clave]
    return acu_datos

def contador_heroe(lista:list) -> int:
    """
    Recibe una lista tipo list y de esa lista
    va sumando 1 al contador por cada heroe en esa lista
    y retorna el contador
    """
    con_datos = 0
    for heroe in lista:
        if len(heroe) > 0 and type(heroe) == type(dict()):
            con_datos += 1
    return con_datos
            
#5.2
def dividir(dividendo:int, divisor:int) -> float:
    """
    Recibe dos enteros, dividendo y divisor 
    los divide si el divisor es mayor a 0 en caso de ser 0 devuelve 0
    Y Si no es 0 retorna la division
    """
    if divisor > 0:
        division = dividendo / divisor
        return division
    else:
        return 0
#5.3
def calcular_promedio(lista:list, clave:str) -> float:
    """
    Recibe una lista tipo list y una clave tipo str
    llama a la funcion sumar_dato_heroe y la guarda en un acumulador y tambien llama a la funcion contador_heroe y la guarda en un contador
    y divide acumulador por contador
    y retona el resultado
    """
    acu_dato = sumar_dato_heroe(lista, clave)
    con_dato = contador_heroe(lista)
    resultado = dividir(acu_dato, con_dato)
    return resultado

#5.4
def stark_calcular_imprimir_promedio_altura(lista:list, clave:str):
    """
    Recibe una lista tipo list, y una clave tipo str
    y llama a calcular_promedio y guarda el promedio en promedio
    despues lo formatea en un string y lo imprime
    si la len de la lista es 0 retorna -1
    """
    if len(lista) > 0:
        promedio = calcular_promedio(lista, clave)
        promedio = round(promedio, 2)
        promedio = "Promedio: {0}".format(promedio)
        imprimir_dato(promedio)
    else:
        return -1

#6.1
def imprimir_menu():
    """
    No recibe nada
    Imprime un menu de opciones y le permite al usuario elegir una opcion para ver lo que desea
    retorna un string
    """
    menu = "Menu de opciones:\n1. Mostrar todos los superheroes\n2. Mostrar superheroes junto a la altura\n3. Mostrar altura maxima\n4. Mostrar altura minima\n5. Mostrar peso maximo\n6. Mostrar peso minimo\n7. Mostrar promedio altura\n8. Salir"
    imprimir_dato(menu)

def validar_entero(numero_str:str) -> int:
    """
    Recibe un numero en string y lo castea a entero
    """
    if type(numero_str) == type(str()) and numero_str.isdigit():
        return True
    else:
        return False
    
def stark_menu_principal():
    """
    Imprime el menu de opciones y le pide al usuario que ingrese una opcion y la valida
    si la validacion da true lo castea si no devuelve -1
    """
    imprimir_menu()
    opcion = input("Opcion: ")
    booleano = validar_entero(opcion)
    if booleano == True:
        opcion = int(opcion)
        return opcion
    else:
        return -1

def stark_marvel_app(lista:list):
    """
    Recibe una list tipo list
    y Ejecuta el programa principal
    """
    stark_normalizar_datos(lista)
    while True:
        opcion = stark_menu_principal()
        if opcion == 1:
            stark_imprimir_nombres_heroes(lista)
        if opcion == 2:
            stark_imprimir_nombres_alturas(lista)
        if opcion == 3:
            stark_calcular_imprimir_heroe(lista, "max", "altura")
        if opcion == 4:
            stark_calcular_imprimir_heroe(lista, "min", "altura")
        if opcion == 5:
            stark_calcular_imprimir_heroe(lista, "max", "peso")
        if opcion == 6:
            stark_calcular_imprimir_heroe(lista, "min", "peso")
        if opcion == 7:
            stark_calcular_imprimir_promedio_altura(lista, "altura")
        if opcion == 8:
            break