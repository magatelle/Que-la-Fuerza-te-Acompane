import csv

class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return (f"Mission Name: {self.nombre}\n"
                f"Destination Planet: {self.planeta_destino}\n"
                f"Starship: {self.nave}\n"
                f"Weapons: {', '.join(self.armas)}\n"
                f"Members: {', '.join(self.integrantes)}\n")


def guardar_misiones_a_csv(misiones, filename="misiones.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['nombre', 'planeta_destino', 'nave', 'armas', 'integrantes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for mision in misiones:
            writer.writerow({
                'nombre': mision.nombre,
                'planeta_destino': mision.planeta_destino,
                'nave': mision.nave,
                'armas': ','.join(mision.armas),
                'integrantes': ','.join(mision.integrantes)
            })

def cargar_misiones_desde_csv(filename="misiones.csv"):
    misiones = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                mision = Mision(
                    nombre=row['nombre'],
                    planeta_destino=row['planeta_destino'],
                    nave=row['nave'],
                    armas=row['armas'].split(','),
                    integrantes=row['integrantes'].split(',')
                )
                misiones.append(mision)
    except FileNotFoundError:
        pass
    return misiones

misiones = []

def crear_mision():
    if len(misiones) >= 5:
        print("\nYou cannot create more than 5 missions.")
        return

    nombre = input("\nMission Name: ")
    planeta_destino = input("Destination Planet: ")
    nave = input("\nStarship: ")
    
    armas = []
    while len(armas) < 7:
        arma = input(f"\nWeapon {len(armas)+1}: ")
        if arma:
            armas.append(arma)
        else:
            break
        if len(armas) < 7:
            add_more = input("\nAdd another weapon? (yes/no): ").strip().lower()
            if add_more not in ['yes', 'y']:
                break
    
    integrantes = []
    while len(integrantes) < 7:
        integrante = input(f"\nMember {len(integrantes)+1}: ")
        if integrante:
            integrantes.append(integrante)
        else:
            break
        if len(integrantes) < 7:
            add_more = input("\nAdd another member? (yes/no): ").strip().lower()
            if add_more not in ['yes', 'y']:
                break
    
    mision = Mision(nombre, planeta_destino, nave, armas, integrantes)
    misiones.append(mision)
    guardar_misiones_a_csv(misiones)
    print("\nMission created successfully!")

def modificar_mision():
    if not misiones:
        print("\nNo missions available to modify.")
        return

    for i, mision in enumerate(misiones):
        print(f"{i + 1}. {mision.nombre}")
    
    indice = input("\nSelect the number of the mission to modify (or press enter to go back):\n-> ").strip()
    if not indice:
        return

    indice = int(indice) - 1
    if indice < 0 or indice >= len(misiones):
        print("\nInvalid mission number.")
        return

    mision = misiones[indice]

    print("1. Modify name")
    print("2. Modify destination planet")
    print("3. Modify starship")
    print("4. Modify weapons")
    print("5. Modify members")
    opcion = input("\nSelect an option to modify (or press enter to go back):\n-> ").strip()
    if not opcion:
        return

    opcion = int(opcion)

    if opcion == 1:
        mision.nombre = input("\nNew name:\n-> ")
    elif opcion == 2:
        mision.planeta_destino = input("\nNew destination planet:\n-> ")
    elif opcion == 3:
        mision.nave = input("\nNew starship: ")
    elif opcion == 4:
        print("1. Add weapons")
        print("2. Remove weapons")
        opcion_arma = input("\nSelect an option (or press enter to go back):\n-> ").strip()
        if not opcion_arma:
            return
        opcion_arma = int(opcion_arma)
        if opcion_arma == 1:
            for _ in range(7 - len(mision.armas)):
                arma = input("\nAdd weapon (leave empty to finish):\n-> ")
                if arma:
                    mision.armas.append(arma)
                else:
                    break
        elif opcion_arma == 2:
            print("Current weapons:")
            for i, arma in enumerate(mision.armas):
                print(f"{i+1}. {arma}")
            arma_a_eliminar = input("\nSelect the number of the weapon to remove (or press enter to go back):\n-> ").strip()
            if not arma_a_eliminar:
                return
            arma_a_eliminar = int(arma_a_eliminar) - 1
            if 0 <= arma_a_eliminar < len(mision.armas):
                mision.armas.pop(arma_a_eliminar)
            else:
                print("Invalid selection.")
    elif opcion == 5:
        print("1. Add members")
        print("2. Remove members")
        opcion_integrante = input("\nSelect an option (or press enter to go back):\n-> ").strip()
        if not opcion_integrante:
            return
        opcion_integrante = int(opcion_integrante)
        if opcion_integrante == 1:
            for _ in range(7 - len(mision.integrantes)):
                integrante = input("Add member (leave empty to finish): ")
                if integrante:
                    mision.integrantes.append(integrante)
                else:
                    break
        elif opcion_integrante == 2:
            print("Current members:")
            for i, integrante in enumerate(mision.integrantes):
                print(f"{i+1}. {integrante}")
            integrante_a_eliminar = input("\nSelect the number of the member to remove (or press enter to go back):\n-> ").strip()
            if not integrante_a_eliminar:
                return
            integrante_a_eliminar = int(integrante_a_eliminar) - 1
            if 0 <= integrante_a_eliminar < len(mision.integrantes):
                mision.integrantes.pop(integrante_a_eliminar)
            else:
                print("\nInvalid selection.")
    else:
        print("\nInvalid option.")

    guardar_misiones_a_csv(misiones)

def visualizar_mision():
    if not misiones:
        print("\nNo missions available to view.")
        return

    for i, mision in enumerate(misiones):
        print(f"{i + 1}. {mision.nombre}")
    
    indice = input("\nSelect the number of the mission to view (or press enter to go back):\n-> ").strip()
    if not indice:
        return

    indice = int(indice) - 1
    if indice < 0 or indice >= len(misiones):
        print("\nInvalid mission number.")
        return

    mision = misiones[indice]
    print(mision)

def guardar_misiones():
    with open("missions.txt", "w") as file:
        for mision in misiones:
            file.write(f"{mision.nombre},{mision.planeta_destino},{mision.nave},{'|'.join(mision.armas)},{'|'.join(mision.integrantes)}\n")
    print("\nMissions saved successfully.")

def cargar_misiones():
    global misiones
    misiones = []
    try:
        with open("missions.txt", "r") as file:
            for line in file:
                nombre, planeta_destino, nave, armas, integrantes = line.strip().split(',')
                misiones.append(Mision(nombre, planeta_destino, nave, armas.split('|'), integrantes.split('|')))
        print("\nMissions loaded successfully.")
    except FileNotFoundError:
        print("\nNo mission file found.")

def menu_misiones():
    while True:
        print("\nMission Menu")
        print("1. Create mission")
        print("2. Modify mission")
        print("3. View mission")
        print("4. Save missions")
        print("5. Load missions")
        print("6. Back to Main Menu")

        opcion = input("Select an option:\n-> ").strip()
        if not opcion:
            continue

        opcion = int(opcion)
        if opcion == 1:
            crear_mision()
        elif opcion == 2:
            modificar_mision()
        elif opcion == 3:
            visualizar_mision()
        elif opcion == 4:
            guardar_misiones()
        elif opcion == 5:
            cargar_misiones()
        elif opcion == 6:
            break
        else:
            print("\nInvalid option")