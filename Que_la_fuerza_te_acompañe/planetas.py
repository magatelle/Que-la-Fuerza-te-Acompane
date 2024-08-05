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