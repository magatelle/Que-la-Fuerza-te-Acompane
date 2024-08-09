class Planeta:
    """
    Clase para representar un planeta en el universo de Star Wars.

    Atributos:
    ----------
    clima : str
        El tipo de clima del planeta.
    creado : str
        La fecha y hora de creación del recurso.
    diametro : str
        El diámetro del planeta.
    editado : str
        La fecha y hora de la última edición del recurso.
    peliculas : list
        Una lista de películas en las que aparece el planeta.
    gravedad : str
        La gravedad del planeta.
    nombre : str
        El nombre del planeta.
    periodo_orbital : str
        El período orbital del planeta.
    poblacion : str
        La cantidad de habitantes del planeta.
    residentes : list
        Una lista de residentes del planeta.
    periodo_de_rotacion : str
        El período de rotación del planeta.
    superficie_del_agua : str
        La superficie de agua del planeta.
    terreno : str
        El tipo de terreno del planeta.
    url : str
        La URL del recurso del planeta en la API SWAPI.
    """
    def __init__(self,
                 climate : str,
                 created : str,
                 diameter : str,
                 edited : str,
                 films : list,
                 gravity : str,
                 name : str,
                 orbital_period : str,
                 population : str,
                 residents : list,
                 rotation_period,
                 surface_water : str,
                 terrain : str,
                 url):
        self.clima = climate
        self.creado = created
        self.diametro = diameter
        self.editado = edited
        self.peliculas = films
        self.gravedad = gravity
        self.nombre = name
        self.periodo_orbital = orbital_period
        self.poblacion = population
        self.residentes = residents
        self.periodo_de_rotacion = rotation_period
        self.superficie_del_agua = surface_water
        self.terreno = terrain
        self.url = url
    
    def mostrar_detalles(self, lista_peliculas, lista_personajes):
        print("   ----------------------------------")
        nombre = " ".join(self.nombre)
        espacios = " "*(19 - (len(nombre)//2))
        print(f"{espacios}{nombre}")
        print("   ----------------------------------")
        print(f"   Orbital Period  ---->  {self.periodo_orbital}")
        print(f"   Rotation Period  ---->  {self.periodo_de_rotacion}")
        print(f"   Population  ---->  {self.poblacion}")
        print(f"   Climate  ---->  {self.clima}")
        
        validacion = False
        print("   Appears in:")
        for pelicula in lista_peliculas:
            url_pel = pelicula.url
            url_pel_planeta = self.peliculas
            if url_pel in url_pel_planeta:
                validacion = True
                print(f"      - {pelicula.título}")
        if validacion == False:
            print("      - None")
        
        validacion2 = False
        print("   People:")
        for personaje in lista_personajes:
            if personaje.url in self.residentes:
                validacion2 = True
                print(f"      - {personaje.nombre}")
        if validacion2 == False:
            print("      - Unknown")