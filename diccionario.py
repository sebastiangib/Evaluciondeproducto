#Yaritza Parra Mazo
#Sebastian Giraldo Berrio

# Crear diccionario
productosDiccionario = {}

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
        precioCrearProducto = int(input("Ingrese el precio del producto $: "))
        
        producto = {
            "nombre": nombreCrearProducto,
            "cantidad": cantidadCrearProducto,
            "precio": precioCrearProducto
        }
        
        productosDiccionario[nombreCrearProducto] = producto
        
        print(f"\nEl producto '{nombreCrearProducto}' ha sido agregado con éxito.")
        
    elif opcion == 2:
        nombreActualizarProducto = input("\nIngrese el nombre del producto que desea actualizar: ") 
        
        if nombreActualizarProducto in productosDiccionario:
            cantidadActualizarProducto = int(input("Ingrese cantidad de productos: ")) 
            precioActualizarProducto = int(input("Ingrese el precio del producto $: "))
            
            productosDiccionario[nombreActualizarProducto]["cantidad"] = cantidadActualizarProducto
            productosDiccionario[nombreActualizarProducto]["precio"] = precioActualizarProducto
            
            print(f"\nProducto '{nombreActualizarProducto}' actualizado correctamente.")
        else:
            print(f"\nProducto '{nombreActualizarProducto}' no encontrado en el inventario.")
        
    elif opcion == 3:
        nombreConsultarProducto = input("\nIngrese el nombre del producto que desea consultar: ") 
        
        if nombreConsultarProducto in productosDiccionario:
            producto = productosDiccionario[nombreConsultarProducto]
            print(f"\nInformación del producto '{nombreConsultarProducto}':")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']}")
        else:
            print(f"\nProducto '{nombreConsultarProducto}' no encontrado en el inventario.")
    elif opcion == 4:
        nombreEliminarProducto = input("\nIngrese el nombre del producto que desea eliminar: ") 
        
        if nombreEliminarProducto in productosDiccionario:
            del productosDiccionario[nombreEliminarProducto]
            print(f"\nProducto '{nombreEliminarProducto}' eliminado correctamente.")
            print(productosDiccionario)
        else:
            print(f"\nProducto '{nombreEliminarProducto}' no encontrado en el inventario.")
    
