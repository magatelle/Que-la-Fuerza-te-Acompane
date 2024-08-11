class Personaje:
    """
    Clase para representar un personaje en el universo de Star Wars.

    Atributos:
    ----------
    cumpleaños : str
        El año de nacimiento del personaje.
    color_ojos : str
        El color de ojos del personaje.
    peliculas : list
        Una lista de películas en las que aparece el personaje.
    género : str
        El género del personaje.
    color_cabello : str
        El color de cabello del personaje.
    estatura : str
        La estatura del personaje.
    planeta_origen : str
        El planeta de origen del personaje.
    masa : str
        La masa del personaje.
    nombre : str
        El nombre del personaje.
    color_piel : str
        El color de piel del personaje.
    creado : str
        La fecha y hora de creación del recurso.
    editado : str
        La fecha y hora de la última edición del recurso.
    especies : list
        Una lsspecies a las que pertenece el personaje.
    naves : list
        Una lista de naves que el personaje ha operado.
    url : str
        La URL del recurso del personaje en la API SWAPI.
    vehículos : list
        Una lista de vehículos que el personaje ha operado.
    """
    def __init__(self, 
                 birth_year : str,  
                 eye_color : str,  
                 films : list,  
                 gender : str,  
                 hair_color : str,  
                 height : str,  
                 homeworld : str,  
                 mass : str,  
                 name : str,  
                 skin_color : str,  
                 created : str,  
                 edited : str,  
                 species : list,  
                 starships : list,  
                 url : str, 
                 vehicles : list):
        self.cumpleaños = birth_year
        self.color_ojos = eye_color
        self.peliculas = films
        self.género = gender
        self.color_cabello = hair_color
        self.estatura = height
        self.planeta_origen = homeworld
        self.masa = mass
        self.nombre = name
        self.color_piel = skin_color
        self.creado = created
        self.editado = edited
        self.especies = species
        self.naves = starships
        self.url = url
        self.vehículos = vehicles
