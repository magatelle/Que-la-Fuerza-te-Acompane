import requests
from funciones import descargar_especies, descargar_naves, descargar_películas, descargar_personajes, descargar_planetas, buscar_personaje, guardar_peliculas_csv, guardar_especies_csv, guardar_naves_csv, guardar_personajes_csv, guardar_planetas_csv
from graficos import graficar_personajes_por_planeta, graficar_caracteristicas_naves, estadisticas_naves


def menú_principal():
    lista_peliculas = descargar_películas()
    lista_especies = descargar_especies()
    lista_planetas = descargar_planetas()
    lista_personajes = descargar_personajes()
    lista_naves = descargar_naves()

    guardar_peliculas_csv(lista_peliculas)
    guardar_especies_csv(lista_especies)
    guardar_planetas_csv(lista_planetas)
    guardar_personajes_csv(lista_personajes)
    guardar_naves_csv(lista_naves)

    titulo_ascii = '''        

███████╗████████╗ █████╗ ██████╗     ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗    ██║    ██║██╔══██╗██╔══██╗██╔════╝
███████╗   ██║   ███████║██████╔╝    ██║ █╗ ██║███████║██████╔╝███████╗
╚════██║   ██║   ██╔══██║██╔══██╗    ██║███╗██║██╔══██║██╔══██╗╚════██║
███████║   ██║   ██║  ██║██║  ██║    ╚███╔███╔╝██║  ██║██║  ██║███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    

███╗   ███╗███████╗████████╗██████╗  ██████╗ ██████╗ ███████╗██████╗ ██╗ █████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║██╔══██╗
██╔████╔██║█████╗     ██║   ██████╔╝██║   ██║██████╔╝█████╗  ██║  ██║██║███████║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██║   ██║██╔═══╝ ██╔══╝  ██║  ██║██║██╔══██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██║     ███████╗██████╔╝██║██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝

    '''
    print(titulo_ascii)

    while True:
        print("")
        print("1. List Films")
        print("2. List Species")
        print("3. List Planets")
        print("4. Search Character") # A partir de la opción 4, todo es CSV (recordatorio para mí misma)
        print("5. Generate Character Birth Planet Chart")
        print("6. Generate Starship Characteristics Charts")
        print("7. Show Starship Statistics")
        print("8. Create Mission") 
        print("9. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("\nList of Films:")
            for pelicula in lista_peliculas:
                print(pelicula)
        
        elif choice == '2':
            print("\nList of Species:")
            for especie in lista_especies:
                print(especie)
        
        elif choice == '3':
            print("\nList of Planets:")
            for planeta in lista_planetas:
                print(planeta)
        
        elif choice == '4':
            buscar_personaje(lista_personajes, lista_planetas, lista_naves, lista_especies)
        
        elif choice == '5':
            graficar_personajes_por_planeta(lista_personajes)

        elif choice == '6':
            graficar_caracteristicas_naves(lista_naves)

        elif choice == '7':
            estadisticas_naves(lista_naves)

        elif choice == '8':
            pass

        elif choice == '9':
            print("Exiting...")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menú_principal()