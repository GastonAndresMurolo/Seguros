from cliente import Cliente
from sistema_seguros import Sistema_seguros

sistema = Sistema_seguros()

while True:
    print("\n--- SISTEMA DE SEGUROS ---")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Acá vamos a registrar un cliente
        nombre=input("Ingrese el nombre: ")
        try:
            dni=int(input("Ingrese el dni"))
        except ValueError:
            print("El DNI debe ser numerico")
            continue
        
        telefono=input("Ingrese el telefono: ")
        
        email=input("Ingrese el mail: ")
        
        cliente=Cliente(nombre,dni,telefono,email)

    elif opcion == "2":
        # Acá vamos a mostrar los clientes
       sistema.mostrar_clientes()
       print("Clientes guardados:", len(sistema.clientes))
        

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida")