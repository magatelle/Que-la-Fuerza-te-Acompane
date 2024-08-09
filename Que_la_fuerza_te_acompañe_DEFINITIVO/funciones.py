import csv
import requests
from naves import Nave
from peliculas import Película
from especies import Especie
from planetas import Planeta
from personajes import Personaje
from vehiculos import Vehiculo

def abrir_db():
    """Descarga la base de datos a traves de SWAPI, y con ella crea los siguientes arcihvos: \n
        - 'peliculas.csv'\n
        - 'especies.csv'\n
        - 'planetas.csv'\n
        - 'personajes.csv'\n
        - 'naves.csv'\n
    Y guarda, en cada uno, la respectiva informacion de cada objeto.
    """
    print("Initiating program...\n")
    
    (lista_peliculas, lista_especies, 
    lista_planetas, lista_personajes, 
    lista_naves, lista_vehiculos) = descargar_data()

    guardar_data(lista_peliculas, lista_especies, 
                lista_planetas, lista_personajes, 
                lista_naves, lista_vehiculos)
    
    return (lista_peliculas, lista_especies, lista_planetas, lista_personajes, lista_naves, lista_vehiculos)

def descargar_data():

    def descargar_películas():

        print("Downloading films...")
        
        # Definir la lista donde guardar las peliculas
        lista_peliculas = []

        # Abrir la primera pagina
        url = "https://swapi.dev/api/films/1/"
        response = requests.get(url)
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la respuesta en formato JSON
            data = response.json()

        else:
            print(f"Error {response.status_code}")
        
        for i in range(1, 7):
            url = f"https://swapi.dev/api/films/{i}/"
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                data = response.json()
                
                personajes = data["characters"]
                creado = data["created"]
                director = data["director"]
                editado = data["edited"]
                episodio_id = int(data["episode_id"])
                apertura_de_texto = data["opening_crawl"]
                planetas = data["planets"]
                productor = data["producer"]
                fecha_lanzamiento = data["release_date"]
                especies = data["species"]
                naves = data["starships"]
                título = data["title"]
                url = data["url"]
                vehículos = data["vehicles"]
            
                # Crear objeto pelicula
                pelicula = Película(personajes, creado, director, editado, 
                                    episodio_id, apertura_de_texto, planetas,
                                    productor, fecha_lanzamiento, especies,
                                    naves, título, url, vehículos)
                lista_peliculas.append(pelicula)
            
            
        lista_ordenada = sorted(lista_peliculas, key=lambda x: x.episodio_id)
        
        print(r"""
    BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    B ___ .____ _ _ _ _  _    .          .        ____ _  _ ___ .___ ____ ____.B
    B |  \ |__| H H 8 #\ @  ___ ___  ___ _ _ ___  @___ #\/8 8__H  H  |__/ |___ B
    B |__/ |  d #_#_# # \@  @_@ @--   @  @-@ @==  @___ #  # # .  _#_ b  \ |___ B
    B    .      \    .             .                       _      .     /\  .  B
    B        \,@"\    .          .    , ,  i-i  "   .     /|        +   ||     B
    B         \                ,   ,  |-|               -==+            ||     B
    B                  ...::.. |-@-|                      :  ...::::::::||.    B
    B ....:::::.......   %%%%' '   '         ...::.:::::.....  ``%%%%%:'||'    B
    B. `::%%%%%%```.  .  .  .  .  .  . ______.  .%%%%%%%%::''''.   .   .|| _.  B
    B . . . . . . . d ._. b . . . .xXXXXX%%%%%%%x. . . . . . . . . . i"|||| |. B
    B..:.:H:.:.:.:.:8xx@xx8:.:.xXXXXXXXXXXX%%%%%%%%%x.:.:.:.:.:.:.:.:|||||:HH..B
    B.::::Hi::::::::Y::":.P'.XXXXXXXXXXXXXXXX%%%%%%%%%%.`::::::::::::|||LL|HH:.B
    B::%:/H|:%:%:%:%:%:%:% xXXXXXXXXXXXXXXXXXX%%%%%%%%%%x %:%:%:%:%:%| ||||HH::B
    B%%%| H||%%%%%%%%%%%%_xXXXXXXXXXXXXXXXXXXX%%%%%%%%%%%x_%%%%%%%%%||LL|||HHH%B
    B___| H||_______.........i..---------____,,..----__,.=-'|`-._.-||||||||HHH|B
    B   | H||          ____,dH.----''''''___ _i,.--'" .-'   `+--/\i._ _________B
    B____,,..--i-''''''     HH|      __,.--'" |H   .-'_______|  |||  `-._      B
    B----------H|----------- __,.--'"        i|H.-'          `.i"||iHH   `-._  B
    B   LS     H|i   __,.--'"----------------.-'              |||||HHH       `-B
    B-------___,.--'"                     .-'                 `._______________B
    BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB   
    """)
            
        print(f"{len(lista_peliculas)} Films successsfully downloaded.")
        
        return lista_ordenada


    def descargar_especies():
        
        print("Downloading species...")
            
        # Definir la lista donde guardar las especies
        lista_especies = []

        # Abrir la primera pagina
        url = "https://swapi.dev/api/species/"
        response = requests.get(url)
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la respuesta en formato JSON
            pagina = response.json()
        
        else:
            print(f"Error {response.status_code}")
        
        # Bucle hasta llegar a la ultima pagina
        while pagina["next"] != None:
            for especie in pagina["results"]:
                altura_promedio = especie["average_height"]
                esperanza_de_vida_prom = especie["average_lifespan"]
                clasificación = especie["classification"]
                creado = especie["created"]
                designación = especie["designation"]
                editado = especie["edited"]
                colores_ojos = especie["eye_colors"]
                colores_cabello = especie["hair_colors"]
                planeta_origen = especie["homeworld"]
                idioma = especie["language"]
                nombre = especie["name"]
                personas = especie["people"]
                películas = especie["films"]
                colores_piel = especie["skin_colors"]
                url = especie["url"]
                
                # Crear objeto pelicula
                especie = Especie(altura_promedio, esperanza_de_vida_prom, 
                                clasificación, creado, 
                                designación, editado, 
                                colores_ojos, colores_cabello, 
                                planeta_origen, idioma,
                                nombre, personas, películas,
                                colores_piel, url)
                lista_especies.append(especie)
                            
            url = pagina["next"]
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                pagina = response.json()
            else:
                print(f"Error {response.status_code}")
                
        # Descargar la ultima pagina despues de romper el bucle
        else: 
            for especie in pagina["results"]:
                altura_promedio = especie["average_height"]
                esperanza_de_vida_prom = especie["average_lifespan"]
                clasificación = especie["classification"]
                creado = especie["created"]
                designación = especie["designation"]
                editado = especie["edited"]
                colores_ojos = especie["eye_colors"]
                colores_cabello = especie["hair_colors"]
                planeta_origen = especie["homeworld"]
                idioma = especie["language"]
                nombre = especie["name"]
                personas = especie["people"]
                películas = especie["films"]
                colores_piel = especie["skin_colors"]
                url = especie["url"]
                
                # Crear objeto pelicula
                especie = Especie(altura_promedio, esperanza_de_vida_prom, 
                                clasificación, creado, 
                                designación, editado, 
                                colores_ojos, colores_cabello, 
                                planeta_origen, idioma,
                                nombre, personas, películas,
                                colores_piel, url)
                lista_especies.append(especie)

        print(r'''
 ___________________________    _____________________    __________________________
|                           |  |         __          |  |        .;:-%/%%%%::      |
|       .----.__            |  |      .-",`"-.       |  |       %:'%%%%'~%%%/:.    |
|      /`:::.   ""-.__      |  |    .' '_  _  `.     |  |      :/  `%~    :\%::.   |
|     |           |'' """\  |  |    | (._, _,) |\    |  |     :' - _ -  -  :%%::.  |
|      \::....   o)  .----' |  |    |  =d:'b= ,;'|   |  |     )-=~>` `<~=- :::=|'  |
|       |:"""':--'-.__""--. |  |    /.   ;_  ,l -|   |  |     ;    | ::     ::')'  |
|      .'  / |        ""))  |  |   |:|.` __ <;l _|   |  |     :  ' ' ::     ::v:'  |
|      | .'.:'         //'  |  |   | ;|_'--`.:l  /   |  |     `.  (_.=:.` /:'::    |
|     .'  ./|               |  |   ;"o8 "--"_|; .8oo.|  |      `./ ::  \  :' :'    |
|     |  '/ |               |  |.o( (8888oo88'  d8888|  |       |  ____ |   ::     |
|    .'    .' __            |  |888. `^|887^' \d88888|  |        \ '~~  .-'.::.    |
|   (`.____,')88bo.         |  |8888o/__ , _.od888888|  |         x---:' .::-'|    |
|  d8o.____.d888888o        |  |88888888888888888LS88|  |      _./ `-._.:'~   :.   |
|_d8888888888LS88888b_______|  |888888888888888880000|  |__.-'~__\___________.'_`._|
''')
                            
        print(f"{len(lista_especies)} Species successsfully downloaded.")
        
        return lista_especies


    def descargar_planetas():
        
        print("Downloading planets...")
            
        # Definir la lista donde guardar los planetas
        lista_planetas = []

        # Abrir la primera pagina
        url = "https://swapi.dev/api/planets/"
        response = requests.get(url)
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la respuesta en formato JSON
            pagina = response.json()
        
        else:
            print(f"Error {response.status_code}")
        
        # Bucle hasta llegar a la ultima pagina
        while pagina["next"] != None:
            for planeta in pagina["results"]:
                
                clima = planeta["climate"]
                creado = planeta["created"]
                diametro = planeta["diameter"]
                editado = planeta["edited"]
                peliculas = planeta["films"]
                gravedad = planeta["gravity"]
                nombre = planeta["name"]
                periodo_orbital = planeta["orbital_period"]
                poblacion = planeta["population"]
                residentes = planeta["residents"]
                periodo_de_rotacion = planeta["rotation_period"]
                superficie_del_agua = planeta["surface_water"]
                terreno = planeta["terrain"]
                url = planeta["url"]
                
                # Crear objeto pelicula
                planeta = Planeta(clima, creado, 
                                diametro, editado,
                                peliculas, gravedad,
                                nombre, periodo_orbital,
                                poblacion, residentes,
                                periodo_de_rotacion, 
                                superficie_del_agua, 
                                terreno, url)
                
                lista_planetas.append(planeta)
                            
            url = pagina["next"]
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                pagina = response.json()
            else:
                print(f"Error {response.status_code}")
                
        # Descargar la ultima pagina despues de romper el bucle
        else: 
            for planeta in pagina["results"]:
                
                clima = planeta["climate"]
                creado = planeta["created"]
                diametro = planeta["diameter"]
                editado = planeta["edited"]
                peliculas = planeta["films"]
                gravedad = planeta["gravity"]
                nombre = planeta["name"]
                periodo_orbital = planeta["orbital_period"]
                poblacion = planeta["population"]
                residentes = planeta["residents"]
                periodo_de_rotacion = planeta["rotation_period"]
                superficie_del_agua = planeta["surface_water"]
                terreno = planeta["terrain"]
                url = planeta["url"]
                
                # Crear objeto pelicula
                planeta = Planeta(clima, creado, 
                                diametro, editado,
                                peliculas, gravedad,
                                nombre, periodo_orbital,
                                poblacion, residentes,
                                periodo_de_rotacion, 
                                superficie_del_agua, 
                                terreno, url)
                
                lista_planetas.append(planeta)

        print(r"""
              
                / ';    .      .                   .         .    .      .
.     .      /"@,/ `.               .           ________   ___   ____
            .   /    `.                     .  / __   __| / _ \ |  _ \
            ;          `.                   ___> \ | |   |  _  ||    /__
           :   .         `-._      .       |_____/ |_| . |_| |_||_|\____|
   .       ;     <=,_c.,_.o=-b         .    _  _  _   ___   ____    ____
     .    :      C=\=\;@<""             .  | |/ \| | / _ \ |  _ \. / ___|
     :    ;   _c'l@< :>\@                  |   .   ||  _  ||    /__> \  .
.    |    \._=-"" \@`"            .         \_/ \_/ |_| |_||_|\______/
      |    `b                 .            .            .
.       #             .                   .         .                   .
        #     . .     __ ..-- ---:::::::::::---.___         . .
    .  .#      __..::::::..::::::::::::::::::::..::""-- ...__         .
....,,o###==-""...::::........::++||#||#+#|+++::::..:::::::::::-._
.     _`%". ........:::.......:::+|||#||||||++:..::::::::::::+++|++-._    .
    -'..   . .......::::......:::+++||##||||||..::...:::::+::::+++|||||-.
.-'. ... ........::::::::.....:::::+++||###|+|+:.::.:++++::++++++||#|#|||#.
 ..  . .::.:::::::::::::::.::.:::::++|||###|||+:+++++++|:+++++||####|#|#|||
.......:+::.:::::::::::::::.:::::::++++||||##+|||++++|#|##++||||######|##|||
:..:.:::|+:::::::::::::::::::::::+++++||||||#:++|#|||####|#|||LS#####|+|##||
:::::::::::::::::::::++++:::::::::+||+|||||||||######@#@#|########@@#||#||||
:::..:.:..:::+:::::+++||++++||::+++||||||||||+||#||||||||||################|
.......::::::++:+:+++|||||##|##++++||||||||||++:+||++++++|#############|####
""")
                            
        print(f"{len(lista_planetas)} Planets successsfully downloaded.")
        
        return lista_planetas


    def descargar_personajes():
        
        print("Downloading characters...")
        
        # Definir la lista donde guardar los personajes
        lista_personajes = []

        # Abrir la primera pagina
        url = "https://swapi.dev/api/people/"
        response = requests.get(url)
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la respuesta en formato JSON
            pagina = response.json()
            
        else:
            print(f"Error {response.status_code}")
        
        # Bucle hasta llegar a la ultima pagina
        while pagina["next"] != None:
            for persona in pagina["results"]:
                
                cumpleaños = persona["birth_year"]
                color_ojos = persona["eye_color"]
                peliculas = persona["films"]
                género = persona["gender"]
                color_cabello = persona["hair_color"]
                estatura = persona["height"]
                planeta_origen = persona["homeworld"]
                masa = persona["mass"]
                nombre = persona["name"]
                color_piel = persona["skin_color"]
                creado = persona["created"]
                editado = persona["edited"]
                especies = persona["species"]
                naves = persona["starships"]
                url = persona["url"]
                vehículos = persona["vehicles"]
                
                # Crear objeto pelicula
                persona = Personaje(cumpleaños, color_ojos, 
                                peliculas, género, color_cabello,
                                estatura, planeta_origen, masa, 
                                nombre, color_piel, creado,
                                editado, especies, naves, url, 
                                vehículos)
                
                lista_personajes.append(persona)
                            
            url = pagina["next"]
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                pagina = response.json()
            else:
                print(f"Error {response.status_code}")
                
        # Descargar la ultima pagina despues de romper el bucle
        else: 
            for persona in pagina["results"]:
                
                cumpleaños = persona["birth_year"]
                color_ojos = persona["eye_color"]
                peliculas = persona["films"]
                género = persona["gender"]
                color_cabello = persona["hair_color"]
                estatura = persona["height"]
                planeta_origen = persona["homeworld"]
                masa = persona["mass"]
                nombre = persona["name"]
                color_piel = persona["skin_color"]
                creado = persona["created"]
                editado = persona["edited"]
                especies = persona["species"]
                naves = persona["starships"]
                url = persona["url"]
                vehículos = persona["vehicles"]
                
                # Crear objeto pelicula
                persona = Personaje(cumpleaños, color_ojos, 
                            peliculas, género, color_cabello,
                            estatura, planeta_origen, masa, 
                            nombre, color_piel, creado,
                            editado, especies, naves, url, 
                            vehículos)
                
                lista_personajes.append(persona)

        print(r"""
                    _    _  __  _  _ _____  ___ ___
                    | /\ | |__| |\ |   |   |___ |  \
                    |/  \| |  | | \|   |   |___ |__/
        F O R   C R I M E S   A G A I N S T   T H E   E M P I R E
________________________  _________________________  _______________________
|        .......         ||      .x%%%%%%x.         ||  ,.------;:~~:-.      |
|      ::::::;;::.       ||     ,%%%%%%%%%%%        || /:.\`;;|||;:/;;:\     |
|    .::;::::;::::.      ||    ,%%%'  )'  \%        ||:')\`:\||::/.-_':/)    |
|   .::::::::::::::      ||   ,%x%) __   _ Y        ||`:`\\\ ;'||'.''/,.:\   |
|   ::`_```_```;:::.     ||   :%%% ~=-. <=~|        ||==`;.:`|;::/'/./';;=   |
|   ::=-) :=-`  ::::     ||   :%%::. .:,\  |        ||:-/-%%% | |%%%;;_- _:  |
| `::|  / :     `:::     ||   `;%:`\. `-' .'        ||=// %wm)..(mw%`_ :`:\  |
|   '|  `~'     ;:::     ||    ``x`. -===-;         ||;;--', /88\ -,- :-~~|  |
|    :-:==-.   / :'      ||     / `:`.__.;          ||-;~~::'`~^~:`::`/`-=:) |
|    `. _    .'.d8:      ||  .d8b.  :: ..`.         ||(;':)%%%' `%%%.`:``:)\ |
| _.  |88bood88888._     || d88888b.  '  /8         ||(\ %%%/dV##Vb`%%%%:`-. |
|~  `-+8888888888P  `-. _||d888888888b. ( 8b       /|| |);/( ;~~~~ :)\`;;.``\|
|-'     ~~^^^^~~  `./8 ~ ||~   ~`888888b  `8b     /:|| //\'/,/|;;|:(: |.|\;|\|
|8b /  /  |   \  \  `8   ||  ' ' `888888   `8. _ /:/||/) |(/ | / \|\\`( )- ` |
|P        `          8   ||'      )88888b   8b |):X ||;):):)/.):|/) (`:`\\`-`|
|                    8b  ||   ~ - |888888   `8b/:/:\||;%/ //;/(\`.':| ::`\\;`|
|                    `8  ||       |888888    88\/~~;||;/~( \|./;)|.|):;\. \\-|
|________/_\___________8_||\_______\88888_.'____\__/||_%__%:__;_:`_;_:_.\%_`_|
L u k e  S k y w a l k e r      H a n   S o l o          C h e w b a c c a
Self-Proclaimed Jedi Knight     Smuggler, Pirate         Smuggler, Pirate
""")
        
        print(f"{len(lista_personajes)} Characters successsfully downloaded.")
        
        return lista_personajes    

    
    def descargar_naves():

        print("Downloading Starships...")

        
        # Definir la lista donde guardar las naves espaciales
        lista_naves = []

        # Abrir la primera pagina
        url = "https://swapi.dev/api/starships/"
        response = requests.get(url)
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la respuesta en formato JSON
            pagina = response.json()
            
        else:
            print(f"Error {response.status_code}")
        
        # Bucle hasta llegar a la ultima pagina
        while pagina["next"] != None:
            for nave in pagina["results"]:
                nombre = nave["name"]
                mglt = nave["MGLT"]
                capacidad_de_carga = nave["cargo_capacity"]
                consumibles = nave["consumables"]
                costo_en_créditos = nave["cost_in_credits"]
                creado = nave["created"]
                tripulacion = nave["crew"]
                editado = nave["edited"]
                calificación_de_hiperimpulsor = nave["hyperdrive_rating"]
                if "," not in nave["length"]:
                    longitud = nave["length"]
                else: 
                    longitud = nave["length"].split(",")
                    longitud = longitud[0] + longitud[1]
                fabricante = nave["manufacturer"]
                velocidad_atmosférica_máxima = nave["max_atmosphering_speed"]
                modelo = nave["model"]
                pasajeros = nave["passengers"]
                peliculas = nave["films"]
                pilotos = nave["pilots"]
                clase_de_nave = nave["starship_class"]
                
                # Crear objeto pelicula
                nave = Nave(mglt, capacidad_de_carga, 
                                consumibles, costo_en_créditos, 
                                creado, tripulacion, editado, 
                                calificación_de_hiperimpulsor, 
                                longitud, fabricante,
                                velocidad_atmosférica_máxima,
                                modelo, nombre, pasajeros,
                                peliculas, pilotos, clase_de_nave)
                lista_naves.append(nave)
                            
            url = pagina["next"]
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                pagina = response.json()
            else:
                print(f"Error {response.status_code}")
                
        # Descargar la ultima pagina despues de romper el bucle
        else: 
            for nave in pagina["results"]:
                nombre = nave["name"]
                mglt = nave["MGLT"]
                capacidad_de_carga = nave["cargo_capacity"]
                consumibles = nave["consumables"]
                costo_en_créditos = nave["cost_in_credits"]
                creado = nave["created"]
                tripulacion = nave["crew"]
                editado = nave["edited"]
                calificación_de_hiperimpulsor = nave["hyperdrive_rating"]
                if "," not in nave["length"]:
                    longitud = nave["length"]
                else: 
                    longitud = nave["length"].split(",")
                    longitud = longitud[0] + longitud[1]
                fabricante = nave["manufacturer"]
                velocidad_atmosférica_máxima = nave["max_atmosphering_speed"]
                modelo = nave["model"]
                pasajeros = nave["passengers"]
                peliculas = nave["films"]
                pilotos = nave["pilots"]
                clase_de_nave = nave["starship_class"]
                
                # Crear objeto pelicula
                nave = Nave(mglt, capacidad_de_carga, 
                                consumibles, costo_en_créditos, 
                                creado, tripulacion, editado, 
                                calificación_de_hiperimpulsor, 
                                longitud, fabricante,
                                velocidad_atmosférica_máxima,
                                modelo, nombre, pasajeros,
                                peliculas, pilotos, clase_de_nave)
                lista_naves.append(nave)

        print(r'''
    .    .     .            +         .         .                 .   .
    .                 .                   .               .           
            .    ,,o         .                  __.o+.          .     
    .            od8^                  .      oo888888P^b           .
        .       ,".o'      .     .             `b^'""`b -`b   .
            ,'.'o'             .   .          t. = -`b -`t.    . 
            ; d o' .        ___          _.--.. 8  -  `b  =`b 
        .  dooo8<       .o:':__;o.     ,;;o88%%8bb - = `b  =`b.    .
    .     |^88^88=. .,x88/::/ | \\`;;;;;;d%%%%%88%88888/%x88888 
        :-88=88%%L8`%`|::|_>-<_||%;;%;8%%=;:::=%8;;\%%%%\8888
    .   |=88 88%%|HHHH|::| >-< |||;%;;8%%=;:::=%8;;;%%%%+|]88        .
        | 88-88%%LL.%.%b::Y_|_Y/%|;;;;`%8%%oo88%:o%.;;;;+|]88  . 
        Yx88o88^^'"`^^%8boooood..-\H_Hd%P%%88%P^%%^'\;;;/%%88
        . `"\^\          ~"""""'      d%P """^" ;   = `+' - P 
.         `.`.b   .                :<%%>  .   :  -   d' - P      .  .
            .`.b     .        .    `788      ,'-  = d' =.'
    .        ``.b.                           :..-  :'  P 
            .    `q.>b         .               `^^^:::::,'       . 
                ""^^               .                     . 
.                                            .               .        .
    .         .           .                 .        +          .
''')
        
        print(f"{len(lista_naves)} Starships successsfully downloaded.")
        
        return lista_naves   


    def descargar_vehiculos():
        print("Downloading Vehicles...")
        
        # Definir la lista donde guardar los vehículos
        lista_vehiculos = []

        # Abrir la primera página
        url = "https://swapi.dev/api/vehicles/"
        response = requests.get(url)
        
        # Verificar que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            
            # Obtener el contenido de la respuesta en formato JSON
            pagina = response.json()
        
        else:
            print(f"Error {response.status_code}")
        
        # Bucle hasta llegar a la última página
        while pagina["next"] != None:
            for vehiculo in pagina["results"]:
                capacidad_de_carga = vehiculo["cargo_capacity"]
                consumibles = vehiculo["consumables"]
                costo_en_créditos = vehiculo["cost_in_credits"]
                creado = vehiculo["created"]
                tripulacion = vehiculo["crew"]
                editado = vehiculo["edited"]
                longitud = vehiculo["length"]
                fabricante = vehiculo["manufacturer"]
                velocidad_atmosférica_máxima = vehiculo["max_atmosphering_speed"]
                modelo = vehiculo["model"]
                nombre = vehiculo["name"]
                pasajeros = vehiculo["passengers"]
                peliculas = vehiculo["films"]
                pilotos = vehiculo["pilots"]
                clase_de_vehiculo = vehiculo["vehicle_class"]
                
                # Crear objeto vehiculo
                vehiculo_obj = Vehiculo(capacidad_de_carga, consumibles, costo_en_créditos, creado, tripulacion, editado, longitud, fabricante, velocidad_atmosférica_máxima, modelo, nombre, pasajeros, peliculas, pilotos, clase_de_vehiculo)
                lista_vehiculos.append(vehiculo_obj)
                            
            url = pagina["next"]
            response = requests.get(url)
            # Verificar que la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener el contenido de la respuesta en formato JSON
                pagina = response.json()
            else:
                print(f"Error {response.status_code}")
                
        # Descargar la última página después de romper el bucle
        if pagina["next"] == None:
            for vehiculo in pagina["results"]:
                capacidad_de_carga = vehiculo["cargo_capacity"]
                consumibles = vehiculo["consumables"]
                costo_en_créditos = vehiculo["cost_in_credits"]
                creado = vehiculo["created"]
                tripulacion = vehiculo["crew"]
                editado = vehiculo["edited"]
                longitud = vehiculo["length"]
                fabricante = vehiculo["manufacturer"]
                velocidad_atmosférica_máxima = vehiculo["max_atmosphering_speed"]
                modelo = vehiculo["model"]
                nombre = vehiculo["name"]
                pasajeros = vehiculo["passengers"]
                peliculas = vehiculo["films"]
                pilotos = vehiculo["pilots"]
                clase_de_vehiculo = vehiculo["vehicle_class"]
                
                # Crear objeto vehiculo y agregar a la lista
                vehiculo_obj = Vehiculo(nombre, modelo, clase_de_vehiculo,
                                        fabricante, longitud, 
                                        costo_en_créditos, tripulacion,
                                        pasajeros, velocidad_atmosférica_máxima,
                                        capacidad_de_carga, consumibles, 
                                        peliculas, pilotos,
                                        url, creado)
                lista_vehiculos.append(vehiculo_obj)
        
        print(f"{len(lista_vehiculos)} Vehicles successfully downloaded.")
        
        return lista_vehiculos


    lista_peliculas = descargar_películas()
    lista_especies = descargar_especies()
    lista_planetas = descargar_planetas()
    lista_personajes = descargar_personajes()
    lista_naves = descargar_naves()
    lista_vehiculos = descargar_vehiculos()
    
    return (lista_peliculas, lista_especies, lista_planetas, lista_personajes, lista_naves, lista_vehiculos)

def guardar_data(lista_peliculas, lista_especies, 
                 lista_planetas, lista_personajes, 
                 lista_naves, lista_vehiculos):

    def guardar_peliculas_csv(lista_peliculas):
        with open('peliculas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Episode number', 'Realease date', 'Opening Crawl', 'Director']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for pelicula in lista_peliculas:
                writer.writerow({
                    'Title': pelicula.título,
                    'Episode number': pelicula.episodio_id,
                    'Realease date': pelicula.fecha_de_lanzamiento,
                    'Opening Crawl': pelicula.apertura_de_texto,
                    'Director': pelicula.director
                })
                
    # Parte de guardado de archivos en .csv
    
    def guardar_especies_csv(lista_especies):
        with open('especies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Heigth', 'Classification', 'Homeworld', 'Language']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for especie in lista_especies:
                writer.writerow({
                    'Name': especie.nombre,
                    'Heigth': especie.altura_promedio,
                    'Classification': especie.clasificación,
                    'Homeworld': especie.planeta_origen,
                    'Language': especie.idioma
                })

    def guardar_planetas_csv(lista_planetas):
        with open('planetas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Orbital period', 'Rotation period', 'Population', 'Climate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for planeta in lista_planetas:
                writer.writerow({
                    'Name': planeta.nombre,
                    'Orbital period': planeta.periodo_orbital,
                    'Rotation period': planeta.periodo_de_rotacion,
                    'Population': planeta.poblacion,
                    'Climate': planeta.clima
                })

    def guardar_personajes_csv(lista_personajes):
        with open('personajes.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Homeworld', 'Episode Title', 'Gender', 'Specie', 'Starships', 'Vehicles']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for personaje in lista_personajes:
                naves = ", ".join(personaje.naves)
                vehiculos = ", ".join(personaje.vehículos)
                writer.writerow({
                    'Name': personaje.nombre,
                    'Homeworld': personaje.planeta_origen,
                    'Episode Title': ", ".join(personaje.peliculas),
                    'Gender': personaje.género,
                    'Specie': ", ".join(personaje.especies),
                    'Starships': naves,
                    'Vehicles': vehiculos
                })

    def guardar_naves_csv(lista_naves):
        with open('naves.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Length', 'Cargo capacity', 'Hyperdrive rating', 'MGLT']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for nave in lista_naves:
                writer.writerow({
                    'Name': nave.nombre,
                    'Length': nave.longitud,
                    'Cargo capacity': nave.capacidad_de_carga,
                    'Hyperdrive rating': nave.calificación_de_hiperimpulsor,
                    'MGLT': nave.mglt
                })   
    
    guardar_peliculas_csv(lista_peliculas)
    guardar_especies_csv(lista_especies)
    guardar_planetas_csv(lista_planetas)
    guardar_personajes_csv(lista_personajes)
    guardar_naves_csv(lista_naves)

# Parte de buscar personajes:

def buscar_personajes(lista_personajes, lista_planetas, 
                      lista_peliculas, lista_especies, 
                      lista_naves, lista_vehiculos):
    nombre_busqueda = input("Enter part of the name of the character to search for:\nType here -> ").lower()
    
    # Buscar personajes que contengan el nombre en el texto
    resultados = [p for p in lista_personajes if nombre_busqueda in p.nombre.lower()]
    
    if resultados:
        print(f"\n{len(resultados)} character(s) were found that match '{nombre_busqueda}':\n")
        for personaje in resultados:
            
            for planeta in lista_planetas:
                if planeta.url == personaje.planeta_origen:
                    personaje_planeta_de_origen = planeta.nombre
            
            personaje_peliculas = []
            for pelicula in lista_peliculas:
                if pelicula.url in personaje.peliculas:
                    personaje_peliculas.append(pelicula.título)
            
            personaje_especies = []
            for especie in lista_especies:
                if especie.url in personaje.especies:
                    personaje_especies.append(especie.nombre)
            
            # Definir la lista donde guardar las naves espaciales
            personaje_naves = []
            for nave in personaje.naves:
                url = nave
                # Abrir la primera pagina
                response = requests.get(url)
                # Verificar que la solicitud fue exitosa (código de estado 200)
                if response.status_code == 200:
                    # Obtener el contenido de la respuesta en formato JSON
                    pagina = response.json()
                    personaje_naves.append(pagina['name'])
                    
                else:
                    print(f"Error {response.status_code}")
            
            personaje_vehiculos = []
            for vehiculo in lista_vehiculos:
                if vehiculo.url in personaje.vehículos:
                    personaje_vehiculos.append(vehiculo.nombre)
            
            print("----------------------------------------")
            print(f"Name: {personaje.nombre}")
            print(f"Birth year: {personaje.cumpleaños}")
            print(f"Eyes color: {personaje.color_ojos}")
            print(f"Hair color: {personaje.color_cabello}")
            print(f"Height: {personaje.estatura} cm")
            print(f"Homeworld: {personaje_planeta_de_origen}")
            print(f"Mass: {personaje.masa} kg")
            print(f"Skin color: {personaje.color_piel}")
            print(f"Gender: {personaje.género}")
            print(f"Films: {', '.join(personaje_peliculas)}")
            print(f"Species: {', '.join(personaje_especies)}")
            print(f"Starships: {', '.join(personaje_naves)}")
            print(f"Vehicles: {', '.join(personaje_vehiculos)}")
            print("----------------------------------------")
    else:
        print(f"No characters were found that match '{nombre_busqueda}'.\n")
        