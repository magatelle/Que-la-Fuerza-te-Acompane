import funciones as f
import gráficos as g
from misiones import menu_misiones

def menú_principal():
    titulo_ascii = r"""
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          \                
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/             .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \               
   .      \            /  /   /__\   \    |         _/.   \    \               
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/               
                               .               .                   .         
   ______________________________________________________________________
  |:..                                                      ``:::&&&&&&HH|
  |&&&:::::..               M E T R O P E D I A                `:::::&&&&|
  |HH&&&&&:::::....._______________________________________________::::::| 
  
"""
    print(titulo_ascii) 
    
    (lista_peliculas, lista_especies, 
     lista_planetas, lista_personajes, 
     lista_naves, lista_vehiculos) = f.abrir_db()

    while True:
        print("""                                 ___________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=|  M A I N  |=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|_ M E N U _|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        print("1. List Films")
        print("2. List Species")
        print("3. List Planets")
        print("4. Search Character") # A partir de la opción 4, todo es CSV (recordatorio para mí misma) # Arreglar
        print("5. Generate Character Birth Planet Chart") 
        print("6. Generate Starship Characteristics Charts") # Revisar
        print("7. Show Starship Statistics")
        print("8. Mission Menú\n")
        print("9. Exit\n")
        
        choice = input("Select an option:\n->  ")
        
        if choice == '1':
            print("\nList of Films:\n")
            for pelicula in lista_peliculas:
                pelicula.mostrar_detalles()
        
        elif choice == '2':
            print("\nList of Species:\n")
            for especie in lista_especies:
                especie.mostrar_detalles(lista_planetas, lista_personajes, lista_peliculas)
        
        elif choice == '3':
            print("\nList of Planets:\n")
            for planeta in lista_planetas:
                planeta.mostrar_detalles(lista_peliculas, lista_personajes)
        
        elif choice == '4':
            f.buscar_personajes(lista_personajes, lista_planetas, 
                                lista_peliculas, lista_especies, 
                                lista_naves, lista_vehiculos)
        
        elif choice == '5':
            g.graficar_personajes_por_planeta(lista_personajes, lista_planetas)

        elif choice == '6':
            g.generar_graficos_naves(lista_naves)

        elif choice == '7':
            g.estadisticas_naves(lista_naves)

        elif choice == '8':
            menu_misiones()
    
        elif choice == '9':
            print("Exiting...")
            break
        
        else:
            print("Invalid option, please try again.")

menú_principal()

                                 