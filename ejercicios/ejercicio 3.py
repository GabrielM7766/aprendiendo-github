#GESTOR DE EMPLEADOS Registar empleados(nombre, salario) calcular promedio salarial, mostrar quien gana más y quien menos.
menu = 0
empleados = []

def registrar_empleado():
    nombre = input("Ingrese el nombre del empleado que desea registrar: ")
    salario = int(input(f"Ingrese el salario del empleado {nombre}: "))
    empleados.append({"nombre": nombre, "salario": salario}) #Agrega a una lista el nombre y el salario con un nombre clave puesto entre comillas.
    
def mostrar_empleados():
    if not empleados:
        print("No hay empleados registrados. ")
    else:
        print("Lista de empleados")
        for i in empleados:
            print(f"- {i['nombre']} gana {i['salario']}")  #Muestra la lista con el formato en que se añadió anteriormente
        print()

def promedio(salarios):
    salarios = [i["salario"] for i in empleados] #Crea una lista nueva incluyendo solo los salarios de cada empleado
    if salarios:
        prom =sum(salarios) /len(salarios)  #Suma los elementos de la lista y luego los divide por la cantidad de elementos en la misma
        print(f"El promedio de los salarios es igual a {prom}$")
    else:
        print("No hay salarios registrados.")
        
        
while menu != 6:
    
    menu = int(input("""Ingrese el proceso que desea realizar: 
                1. Registrar un nuevo empleado. (nombre y salario) 
                2. Mostrar lista de empleados
                3. Mostrar promedio de salarios
                4. Mostrar salario más alto
                5. Mostrar salario más bajo
                6. Salir
                --> """))

    if menu ==1:
        registrar_empleado()
        print(F"El empleado que ha añadido es: {empleados[-1]}") #-1 Muestra el último elemento presente en la lista.
    elif menu == 2:
        mostrar_empleados()
    elif menu == 3:
        promedio(empleados)
    elif menu == 4:
        salario_maximo = max(i["salario"] for i in empleados) # Recorre la lista de salarios y busca el elemento más alto.
        print(f"El salario más alto es {salario_maximo}")
    elif menu == 5:
        salario_minimo = min(i["salario"] for i in empleados)
        print(f"El salario más bajo es {salario_minimo}")
    elif menu > 6:
        print("Error. Ingrese un número menor a 6.")