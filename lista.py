#Yaritza Parra Mazo
#Sebastian Giraldo Berrio

productosLista = []

while True:
    print("\nOpciones disponibles:")
    print("\n1. Crear un nuevo producto")
    print("2. Actualizar un producto")
    print("3. Consultar un producto")
    print("4. Eliminar un producto")

    opcion = int(input("\nSeleccione una opción (1/2/3/4): "))

    if opcion == 1:
        nombreCrearProducto = input("\nIngrese el nombre del producto que desea agregar: ")
        cantidadCrearProducto = int(input("Ingrese cantidad de productos: "))
        precioCrearProducto = float(input("Ingrese el precio del producto $: "))

        producto = {
            "nombre": nombreCrearProducto,
            "cantidad": cantidadCrearProducto,
            "precio": precioCrearProducto
        }

        productosLista.append(producto)

        print(f"\nEl producto '{nombreCrearProducto}' ha sido agregado con éxito.")

    elif opcion == 2:
        nombreActualizarProducto = input("\nIngrese el nombre del producto que desea actualizar: ")

        producto_encontrado = False
        for producto in productosLista:
            if producto["nombre"] == nombreActualizarProducto:
                cantidadActualizarProducto = int(input("Ingrese cantidad de productos: "))
                precioActualizarProducto = float(input("Ingrese el precio del producto $: "))

                producto["cantidad"] = cantidadActualizarProducto
                producto["precio"] = precioActualizarProducto

                print(f"\nProducto '{nombreActualizarProducto}' actualizado correctamente.")
                producto_encontrado = True
                break

        if not producto_encontrado:
            print(f"\nProducto '{nombreActualizarProducto}' no encontrado en el inventario.")

    elif opcion == 3:
        nombreConsultarProducto = input("\nIngrese el nombre del producto que desea consultar: ")

        producto_encontrado = False
        for producto in productosLista:
            if producto["nombre"] == nombreConsultarProducto:
                print(f"\nInformación del producto '{nombreConsultarProducto}':")
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Precio: ${producto['precio']}")
                producto_encontrado = True
                break

        if not producto_encontrado:
            print(f"\nProducto '{nombreConsultarProducto}' no encontrado en el inventario.")

    elif opcion == 4:
        productosLista.clear()
        print("Lista de productos eliminada correctamente")
