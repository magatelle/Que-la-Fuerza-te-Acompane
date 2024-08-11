class Película:
    """
    Clase para representar una película en el universo de Star Wars.

    Atributos:
    ----------
    personajes : list
        Una lista de personajes que aparecen en la película.
    creado : str
        La fecha y hora de creación del recurso.
    director : str
        El nombre del director de la película.
    editado : str
        La fecha y hora de la última edición del recurso.
    episodio_id : int
        El número del episodio de la película.
    apertura_de_texto : str
        El texto de apertura de la película.
    planetas : list
        Una lista de planetas que aparecen en la película.
    productor : str
        El nombre del productor de la película.
    fecha_de_lanzamiento : str
        La fecha de lanzamiento de la película.
    especies : list
        Una lista de especies que aparecen en la película.
    naves : list
        Una lista de naves que aparecen en la película.
    título : str
        El título de la película.
    url : str
        La URL del recurso de la película en la API SWAPI.
    vehículos : list
        Una lista de vehículos que aparecen en la película.
    """
    def __init__(self, 
                 characters : list, 
                 created : str, 
                 director : str, 
                 edited : str, 
                 episode_id : int, 
                 opening_crawl : str, 
                 planets : list, 
                 producer : str, 
                 release_date : str, 
                 species : list, 
                 starships : list, 
                 title : str, 
                 url : str, 
                 vehicles : list):
        self.personajes = characters
        self.creado = created
        self.director = director
        self.editado = edited
        self.episodio_id = episode_id
        self.apertura_de_texto = opening_crawl
        self.planetas = planets
        self.productor = producer
        self.fecha_de_lanzamiento = release_date
        self.especies = species
        self.naves = starships
        self.título = title
        self.url = url
        self.vehículos = vehicles

    def mostrar_detalles(self):
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        espacios = " "*(23 - (len(self.título)//2))
        print(f"{espacios}{self.título}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f" Episode {self.episodio_id}")
        print(f" {self.fecha_de_lanzamiento}")
        print("")
        print(f" {self.apertura_de_texto}")
        print("")
        print(f" Director: {self.director}")
        print("______________________________________________")