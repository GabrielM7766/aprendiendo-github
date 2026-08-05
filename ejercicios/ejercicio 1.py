saldo = 0  # Saldo inicial

def depositar():
    global saldo #Hace que se pueda usar la variable externa a la función sin crear una nueva con el mismo nombre.
    try:
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {saldo}$\n") #\n es para realizar un salto de línea.
        else:
            print("El monto debe ser mayor que cero.\n")
    except ValueError: #ValueError se usa para evitar que el programa se cierre en caso de errores al insertar datos
        print("Entrada inválida. Ingrese un número.\n")

def retirar():
    global saldo
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.\n")
        elif monto > saldo: #Si el usuario desea retirar más dinero del que posee mostrar el mensaje:
            print("Fondos insuficientes.\n")
        else:
            saldo -= monto # -= es lo mismo que decir <<saldo = saldo - monto>>
            print(f"Retiro exitoso. Nuevo saldo: {saldo:.2f}$\n")
    except ValueError:
        print("Entrada inválida. Ingrese un número.\n")

def consultar_saldo():
    print(f"Su saldo actual es: {saldo:.2f}$\n")

menu = 0
while menu != 4:
    menu = int(input("""=== Bienvenido al cajero. ¿Qué desea realizar?
                    1. Depositar dinero
                    2. Retirar dinero
                    3. Consultar saldo
                    4. Salir
                    --> """))


    if menu == 1:
        depositar()
    elif menu == 2:
        retirar()
    elif menu == 3:
        consultar_saldo()
    elif menu == 4:
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.\n")

