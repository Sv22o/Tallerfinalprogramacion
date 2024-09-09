import json
with open("inventario.json", "r") as file:
    productos = json.load(file)

# Muestra la lista completa de productos
def mostrarProductos():
 print('--- Inventario de Productos ---')
 for producto in productos:
    print(f'Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, '
                f'Cantidad: {producto.get('cantidad')}')

# Muestra los datos del producto solicitado
def buscarProducto():
   buscar = input("Ingrese el nombre del producto: ")
   buscar = buscar.capitalize()
   for producto in productos:
      if buscar == producto["nombre"]:
        print(f'Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, '
              f'Cantidad: {producto.get('cantidad')}')
        return
   print("\n*** Producto no hallado ***")

# Agrega un nuevo producto al inventario
def crearProducto():
   nombre = input('Ingrese el nombre del producto: ')
   nombre = nombre.capitalize()

   for producto in productos: # Verifica si el producto está en inventario
        if nombre == producto["nombre"]:
            print('\n*** El producto ya se encuentra registrado ***')
            return

   precio = float(input('Ingrese el precio del producto: '))
   cantidad = int(input('Ingrese la cantidad del producto: '))

   # Agrega el nuevo producto en caso de no estar registrado
   nuevo_producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
   productos.append(nuevo_producto) # Agrega el nuevo producto al archivo pero no lo exporta

   with open("inventario.json", "w") as outifle:
      json.dump(productos, outifle, indent=4) # Actualiza el inventario exportando el nuevo producto
      print(f'\n*** El producto {nombre} se agregó al inventario ***')

# Modifica un producto
def modificarProducto():
   producto_a_modificar = input('Ingrese el nombre del producto: ')
   producto_a_modificar = producto_a_modificar.capitalize()

   for producto in productos:
      if producto_a_modificar == producto["nombre"]:
         print(f'Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, '
              f'Cantidad: {producto.get('cantidad')}')
         
         dato_a_modificar = int(input(f'''\n--- Información del Producto --- 
         1. Nombre
         2. Precio
         3. Cantidad
         Que información desea modificar? '''))

         if dato_a_modificar == 1:
            nombre_nuevo = input('\nIngrese el nuevo nombre del producto: ')
            producto["nombre"] = nombre_nuevo.capitalize()
            with open("inventario.json", "w") as outfile:
               json.dump(productos, outfile, indent=4)
               print('\n*** El nombre se modificó correctamente ***')
            return
            
         elif dato_a_modificar == 2:
            precio_nuevo = float(input('\nIngrese el nuevo precio del producto: '))
            producto["precio"] = precio_nuevo
            with open("inventario.json", "w") as outfile: # Se abre el json en cada opcion para evitar errores
               json.dump(productos, outfile, indent=4)   
               print('\n*** El precio se modificó correctamente ***')
            return

         elif dato_a_modificar == 3:
            cantidad_nuevo = int(input('\nIngrese la nueva cantidad del producto: '))
            producto["cantidad"] = cantidad_nuevo
            with open("inventario.json", "w") as outfile:
               json.dump(productos, outfile, indent=4)
               print('\n*** La cantidad se modificó correctamente ***')
            return

         else: 
            print('\n*** Opción invalida ***')
            return
   print('\n*** Producto no hallado ***')

# Elimina un producto del inventario
def eliminarProducto():
   producto_a_eliminar = input('Ingrese el nombre del producto: ')
   producto_a_eliminar = producto_a_eliminar.capitalize()

   for producto in productos:
      if producto_a_eliminar == producto["nombre"]:
         with open("inventario.json", "w") as outfile:
            productos.remove(producto)
            json.dump(productos, outfile, indent=4)
            print('\n*** Producto eliminado correctamente ***')
            return
   print('\n*** Producto no hallado ***')

# Menu Principal
if __name__ == '__main__':
    while True:
        print(f'''\n                   --- Menú ---
              1. Mostrar Inventario
              2. Mostrar Producto
              3. Agregar Producto
              4. Modificar Producto
              5. Eliminar Producto
              6. Salir ''') 
        
        opcion = int(input('\nQue desea hacer? '))

        if opcion == 1:
            mostrarProductos()
        
        elif opcion == 2:
            buscarProducto()
        
        elif opcion == 3:
            crearProducto()    
        
        elif opcion == 4:
            modificarProducto()
        
        elif opcion == 5:
           eliminarProducto()
        
        elif opcion == 6:
           print('\n*** Hasta luego! ***')
           break
        
        else:
           print('\n*** Opción invalida ***')
               