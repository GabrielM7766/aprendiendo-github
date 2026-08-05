productos = []
IVA = 0.19  # 19% de IVA, al escribirlo en mayúsculas se crea una constante la cual nunca cambia su valor.
DESC = 0.10  # 10% de descuento

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input(f"Ingrese el precio de '{nombre}': "))
        productos.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' agregado por {precio:.2f}$\n") #:.2f es para definir cuantos decimales debe incluir el resultado impreso.
    except ValueError:
        print("Error: El precio debe ser un número.\n")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.\n")
    else:
        print("Lista de productos:")
        for i in productos:
            print(f"- {i['nombre']}: {i['precio']:.2f}$")
        print()

def calcular_total():
    if not productos:
        print("No hay productos para calcular.\n")
        return
    subtotal = sum(p["precio"] for p in productos)
    iva = subtotal * IVA
    descuento = subtotal * DESC
    total = subtotal + iva - descuento

    print("Resumen de compra:")
    print(f"Subtotal: {subtotal:.2f}$")
    print(f"IVA (19%): {iva:.2f}$")
    print(f"Descuento (10%): {descuento:.2f}$")
    print(f"Total a pagar: {total:.2f}$\n")

menu = 0
while menu != 4:
    menu = int(input("""=== Simulador de compras ===
                    1. Agregar producto
                    2. Mostrar producto
                    3. Calcular total con IVA y descuento
                    4. Salir
                    --> """))

    if menu == 1:
        agregar_producto()
    elif menu == 2:
        mostrar_productos()
    elif menu == 3:
        calcular_total()
    else:
        print("Opción inválida. Intente de nuevo.\n")
