import random # importamos libreria random para generar números aleatorios

# Diccionario para almacenar los tickets: {numero: {datos}}
tickets = {}

#definimos la función para generar un número de ticket aleatorio:
def generar_numero():
    """Genera un número de ticket random entre 1000 y 9999 que no esté en uso."""
    while True:
        numero = random.randint(1000, 9999)
        if numero not in tickets:
            return numero
#definimos la función para mostrar un ticket por pantalla:
def mostrar_ticket(numero):
    """Muestra por pantalla un ticket dado su número."""
    t = tickets[numero]
    print("\n" + "="*45)
    print("         TICKET DE SOPORTE")
    print("="*45)
    print(f"  N° de Ticket : {numero}")
    print(f"  Nombre       : {t['nombre']}")
    print(f"  Sector       : {t['sector']}")
    print(f"  Asunto       : {t['asunto']}")
    print(f"  Problema     : {t['problema']}")
    print("="*45)

#definimos la función para dar de alta un ticket:
def alta_ticket():
    """Flujo de alta de ticket."""
    while True:
        print("\n--- ALTA DE TICKET ---")

        nombre = input("  Nombre      : ").strip()
        while not nombre:
            print("  ⚠ El nombre no puede estar vacío.")
            nombre = input("  Nombre      : ").strip()

        sector = input("  Sector      : ").strip()
        while not sector:
            print("  ⚠ El sector no puede estar vacío.")
            sector = input("  Sector      : ").strip()

        asunto = input("  Asunto      : ").strip()
        while not asunto:
            print("  ⚠ El asunto no puede estar vacío.")
            asunto = input("  Asunto      : ").strip()

        problema = input("  Problema    : ").strip()
        while not problema:
            print("  ⚠ El problema no puede estar vacío.")
            problema = input("  Problema    : ").strip()

        # Guardar ticket
        numero = generar_numero()
        tickets[numero] = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema
        }

        # Mostrar ticket generado
        mostrar_ticket(numero)
        print(f"\n  ⚠  ¡IMPORTANTE! Recuerde su número de ticket: {numero}")
        print("="*45)

        # Preguntar si desea crear otro
        while True:
            opcion = input("\n  ¿Desea crear otro ticket? (s/n): ").strip().lower()
            if opcion == "s":
                break           # vuelve al inicio del while -> nueva alta
            elif opcion == "n":
                return          # vuelve al menú principal
            else:
                print("  ⚠ Por favor ingrese 's' o 'n'.")

#definimos la función para leer un ticket por número:
def leer_ticket():
    """Flujo de lectura de ticket por número."""
    while True:
        print("\n--- LEER TICKET ---")

        if not tickets:
            print("  ⚠ No hay tickets registrados aún.")
            return

        try:
            numero = int(input("  Ingrese el número de ticket: ").strip())
        except ValueError:
            print("  ⚠ Debe ingresar un número válido.")
            continue

        if numero in tickets:
            mostrar_ticket(numero)
        else:
            print(f"  ⚠ No se encontró ningún ticket con el número {numero}.")

        # Preguntar si desea leer otro
        while True:
            opcion = input("\n  ¿Desea leer otro ticket? (s/n): ").strip().lower()
            if opcion == "s":
                break           # vuelve al inicio del while -> nueva búsqueda
            elif opcion == "n":
                return          # vuelve al menú principal
            else:
                print("  ⚠ Por favor ingrese 's' o 'n'.")

#Menu de la ticketa:
def menu():
    """Menú principal."""
    while True:
        print("\n" + "="*45)
        print("        SISTEMA DE TICKETERA V1.0")
        print("="*45)
        print("  >> 1. Alta de Ticket")
        print("  >> 2. Leer Ticket")
        print("  >> 0. Salir")
        print("="*45)

        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "0":
            # Confirmación antes de salir
            while True:
                confirmacion = input("  ¿Está seguro que desea salir (s/n)?: ").strip().lower()
                if confirmacion == "s":
                    print("  ¡Hasta pronto!")
                    return  # Sale del menú principal
                elif confirmacion == "n":
                    break   # Vuelve al menú principal
                else:
                    print("  ⚠ Por favor ingrese 's' o 'n'.")
        else:
            print("  ⚠ Opción inválida. Por favor, ingrese 1, 2 o 0.")

# Iniciar el programa
menu()
