import random
import string 

def generar_pass(caracteres, largo):
    """Genera la contraseña con los siguientes caracteres"""
    return ''.join(random.choice(caracteres) for _ in range(largo))

def menu():
    print("\n-----LE DAMOS LA BIENVENIDA------")
    print("-----Generador de Contraseñas----")
    print(">>-----------------------------<<")
    print("Seleccione una de las siguientes opciones:")
    print(">> 1. Generar contraseña solo de letras.")
    print(">> 2. Generar contraseña solo de números.")
    print(">> 3. Generar contraseña letras y números.")
    print(">> 4. Generar contraseña letras, números y caracteres.")
    print(">> 0. Salir.")

# Bandera para saber si hace falta mostrar el menú principal
mostrar_menu_inicio = True

while True:
    if mostrar_menu_inicio:
        menu()
        mostrar_menu_inicio = False  # Lo apagamos para que no se repita solo

    opcion = input("\nEscriba la opción seleccionada: ").strip()

    if opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    elif opcion in ("1", "2", "3", "4"):
        if opcion == "1":
            caracteres_disponibles = string.ascii_letters
        elif opcion == "2":
            caracteres_disponibles = string.digits
        elif opcion == "3":
            caracteres_disponibles = string.ascii_letters + string.digits
        elif opcion == "4":
            caracteres_disponibles = string.ascii_letters + string.digits + string.punctuation

        largo_input = input("¿Cuántos caracteres debe tener la contraseña? ").strip()
        
        if largo_input.isdigit():
            largo = int(largo_input)
            if largo <= 0:
                print("Cuidado: El largo debe ser mayor a 0.")
                mostrar_menu_inicio = True
                continue
        else:
            print("Por favor ingrese un número entero válido.")
            mostrar_menu_inicio = True
            continue

        # Generar y mostrar el resultado
        resultado = generar_pass(caracteres_disponibles, largo)
        print(f"\n✅ Contraseña generada: {resultado}\n")

        # FRENADO REAL: Acá se clava a preguntar antes de cualquier otra acción
        otra_contrasena = input("¿Desea generar otra contraseña? (s/n): ").strip().lower()
        
        if otra_contrasena == "n":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            # Si quiere seguir ('s'), volvemos a encender el menú para la próxima vuelta
            mostrar_menu_inicio = True
            
    else:
        print("Opción no válida. Por favor elija entre 0 y 4.")
        mostrar_menu_inicio = True