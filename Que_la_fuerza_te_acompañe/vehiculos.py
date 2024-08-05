class Vehiculo:
    """
    Clase para representar un vehículo en el universo de Star Wars.

    Atributos:
    ----------
    nombre : str
        El nombre del vehículo.
    modelo : str
        El modelo del vehículo.
    clase_nave : str
        La clase del vehículo o nave.
    fabricante : str
        El fabricante del vehículo.
    longitud : str
        La longitud del vehículo.
    costo_en_creditos : str
        El costo del vehículo en créditos.
    tripulacion : str
        La cantidad de tripulantes necesarios para operar el vehículo.
    pasajeros : str
        La cantidad de pasajeros que puede llevar el vehículo.
    velocidad_maxima_atmosfera : str
        La velocidad máxima que el vehículo puede alcanzar en la atmósfera.
    capacidad_carga : str
        La capacidad de carga del vehículo.
    consumibles : str
        El tiempo que el vehículo puede operar antes de necesitar reabastecimiento.
    peliculas : list
        Una lista de películas en las que aparece el vehículo.
    pilotos : list
        Una lista de pilotos que han operado el vehículo.
    url : str
        La URL del recurso del vehículo en la API SWAPI.
    creado : str
        La fecha y hora de creación del recurso.
    editado : str
        La fecha y hora de la última edición del recurso.
    """
    def __init__(self,
                 name: str,
                 model: str,
                 vehicle_ship: str,
                 manufacturer: str,
                 length: str,
                 cost_in_credits: str,
                 crew: str,
                 passengers: str,
                 max_atmosphering_speed: str,
                 cargo_capacity: str,
                 consumables: str,
                 films: list,
                 pilots: list,
                 url: str,
                 created: str,
                 edited: str):
        self.nombre = name
        self.modelo = model
        self.clase_nave = vehicle_ship
        self.fabricante = manufacturer
        self.longitud = length
        self.costo_en_creditos = cost_in_credits
        self.tripulacion = crew
        self.pasajeros = passengers
        self.velocidad_maxima_atmosfera = max_atmosphering_speed
        self.capacidad_carga = cargo_capacity
        self.consumibles = consumables
        self.peliculas = films
        self.pilotos = pilots
        self.url = url
        self.creado = created
        self.editado = edited