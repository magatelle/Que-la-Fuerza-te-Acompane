class Especie:
    def __init__(self,
                 average_height : str,
                 average_lifespan : str,
                 classification : str,
                 created : str,
                 designation : str,
                 edited : str,
                 eye_colors : str,
                 hair_colors : str,
                 homeworld : str,
                 language : str,
                 name : str,
                 people : list,
                 films : list,
                 skin_colors : str,
                 url : str):
        self.altura_promedio = average_height
        self.esperanza_de_vida_prom = average_lifespan
        self.clasificación = classification
        self.creado = created
        self.designación = designation
        self.editado = edited
        self.colores_ojos = eye_colors
        self.colores_cabello = hair_colors
        self.planeta_origen = homeworld
        self.idioma = language
        self.nombre = name
        self.personas = people
        self.películas = films
        self.colores_piel = skin_colors
        self.url = url
    
    def mostrar_detalles(self, lista_planetas, lista_personajes, lista_peliculas):
        print("  ----------------------------------")
        nombre = " ".join(self.nombre)
        espacios = " "*(17 - (len(nombre)//2))
        print(f"{espacios}{nombre}")
        print("  ----------------------------------")
        if self.altura_promedio != "n/a":
            print(f"  Average height -----> {self.altura_promedio} cm.") 
        else: 
            print(f"  Average height -----> {self.altura_promedio}")
        print(f"  Classification -----> {self.clasificación}")
        
        validacion = False
        for planeta in lista_planetas:
            if planeta.url == self.planeta_origen:
                planeta_origen = planeta.nombre
                validacion = True
        if validacion == False:
            planeta_origen='Unknown'

        print(f"  Homeworld -----> {planeta_origen}")
        
        for personaje in lista_personajes:
            especie = self.url
            per_esp = personaje.especies
            if especie in per_esp:
            
                num_apariciones = ""
                for pelicula in lista_peliculas:
                    if pelicula.url in personaje.peliculas:
                        num_apariciones += f" {pelicula.episodio_id}"
                if len(num_apariciones) > 2 :
                    esp = 26 - len(personaje.nombre) - len(num_apariciones)
                    print(f"  {personaje.nombre}"+"."*esp + "Episodes" + num_apariciones)
                else:
                    esp = 26 - len(personaje.nombre) - len(num_apariciones)
                    print(f"  {personaje.nombre}"+"."*esp + "Episode" + num_apariciones)