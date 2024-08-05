import csv
import requests
from naves import Nave
from peliculas import Película
from especies import Especie
from planetas import Planeta
from personajes import Personaje

def descargar_películas():

    print("Downloading Films...")
    
    # Definir la lista donde guardar las peliculas
    lista_peliculas = []

    # Abrir la primera pagina
    url = "https://www.swapi.tech/api/films/"
    response = requests.get(url)
    # Verificar que la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido de la respuesta en formato JSON
        data = response.json()
        
    else:
        print(f"Error {response.status_code}")
    
    for pelicula in data["result"]:
        personajes = pelicula["properties"]["characters"]
        creado = pelicula["properties"]["created"]
        director = pelicula["properties"]["director"]
        editado = pelicula["properties"]["edited"]
        episodio_id = int(pelicula["properties"]["episode_id"])
        apertura_de_texto = pelicula["properties"]["opening_crawl"]
        planetas = pelicula["properties"]["planets"]
        productor = pelicula["properties"]["producer"]
        fecha_lanzamiento = pelicula["properties"]["release_date"]
        especies = pelicula["properties"]["species"]
        naves = pelicula["properties"]["starships"]
        título = pelicula["properties"]["title"]
        url = pelicula["properties"]["url"]
        vehículos = pelicula["properties"]["vehicles"]
        
        # Crear objeto pelicula
        pelicula = Película(personajes, creado, director, editado, 
                            episodio_id, apertura_de_texto, planetas,
                            productor, fecha_lanzamiento, especies,
                            naves, título, url, vehículos)
        lista_peliculas.append(pelicula)
        
    print(f"{len(lista_peliculas)} Films successsfully downloaded.")
    
    return lista_peliculas


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
                        
    print(f"{len(lista_planetas)} Planets successsfully downloaded.")
    
    return lista_planetas


def descargar_personajes():
    
    print("Downloading Characters...")
    
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
    
    print(f"{len(lista_personajes)} Characters successsfully downloaded.")
    
    return lista_personajes           

# Parte para buscar personajes:

def buscar_personaje(lista_personajes, lista_planetas, lista_naves, lista_especies):
    nombre_busqueda = input("Ingrese el nombre del personaje a buscar: ").lower()
    resultados = []

    for personaje in lista_personajes:
        if nombre_busqueda in personaje.nombre.lower():
            resultados.append(personaje)

    if resultados:
        for personaje in resultados:
            print(personaje.mostrar_informacion_detallada(lista_planetas, lista_naves, lista_especies))
            print("------------------------------")
    else:
        print("No se encontraron personajes que coincidan con el criterio de búsqueda.")
 
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
            mglt = nave["MGLT"]
            capacidad_de_carga = nave["cargo_capacity"]
            consumibles = nave["consumables"]
            costo_en_créditos = nave["cost_in_credits"]
            creado = nave["created"]
            tripulacion = nave["crew"]
            editado = nave["edited"]
            calificación_de_hiperimpulsor = nave["hyperdrive_rating"]
            longitud = nave["length"]
            fabricante = nave["manufacturer"]
            velocidad_atmosférica_máxima = nave["max_atmosphering_speed"]
            modelo = nave["model"]
            nombre = nave["name"]
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
            mglt = nave["MGLT"]
            capacidad_de_carga = nave["cargo_capacity"]
            consumibles = nave["consumables"]
            costo_en_créditos = nave["cost_in_credits"]
            creado = nave["created"]
            tripulacion = nave["crew"]
            editado = nave["edited"]
            calificación_de_hiperimpulsor = nave["hyperdrive_rating"]
            longitud = nave["length"]
            fabricante = nave["manufacturer"]
            velocidad_atmosférica_máxima = nave["max_atmosphering_speed"]
            modelo = nave["model"]
            nombre = nave["name"]
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
    
    print(f"{len(lista_naves)} Starships successsfully downloaded.")
    
    return lista_naves   

# Revisar esto a fondo

def guardar_peliculas_csv(lista_peliculas):
    with open('peliculas.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Título', 'Número del episodio', 'Fecha de lanzamiento', 'Opening Crawl', 'Director']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pelicula in lista_peliculas:
            writer.writerow({
                'Título': pelicula.titulo,
                'Número del episodio': pelicula.episodio_id,
                'Fecha de lanzamiento': pelicula.fecha_lanzamiento,
                'Opening Crawl': pelicula.apertura_de_texto,
                'Director': pelicula.director
            })

def guardar_especies_csv(lista_especies):
    with open('especies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Altura', 'Clasificación', 'Planeta de origen', 'Lengua materna']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for especie in lista_especies:
            planeta_origen = especie.planeta_origen  # Asumiendo que es un ID o URL
            idioma = especie.idioma
            writer.writerow({
                'Nombre': especie.nombre,
                'Altura': especie.altura_promedio,
                'Clasificación': especie.clasificación,
                'Planeta de origen': planeta_origen,
                'Lengua materna': idioma
            })

def guardar_planetas_csv(lista_planetas):
    with open('planetas.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Período de órbita', 'Período de rotación', 'Cantidad de habitantes', 'Tipo de clima']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for planeta in lista_planetas:
            writer.writerow({
                'Nombre': planeta.nombre,
                'Período de órbita': planeta.periodo_orbital,
                'Período de rotación': planeta.periodo_de_rotacion,
                'Cantidad de habitantes': planeta.poblacion,
                'Tipo de clima': planeta.clima
            })

def guardar_personajes_csv(lista_personajes):
    with open('personajes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Planeta de origen', 'Títulos de los episodios', 'Género', 'Especie', 'Naves', 'Vehículos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for personaje in lista_personajes:
            naves = ", ".join(personaje.naves)
            vehiculos = ", ".join(personaje.vehiculos)
            writer.writerow({
                'Nombre': personaje.nombre,
                'Planeta de origen': personaje.planeta_origen,
                'Títulos de los episodios': ", ".join(personaje.peliculas),
                'Género': personaje.género,
                'Especie': ", ".join(personaje.especies),
                'Naves': naves,
                'Vehículos': vehiculos
            })

def guardar_naves_csv(lista_naves):
    with open('naves.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Longitud', 'Capacidad de carga', 'Clasificación de hiperimpulsor', 'MGLT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for nave in lista_naves:
            writer.writerow({
                'Nombre': nave.nombre,
                'Longitud': nave.longitud,
                'Capacidad de carga': nave.capacidad_de_carga,
                'Clasificación de hiperimpulsor': nave.calificación_de_hiperimpulsor,
                'MGLT': nave.mglt
            })