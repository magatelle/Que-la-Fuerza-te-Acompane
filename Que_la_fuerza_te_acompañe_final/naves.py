class Nave:
    """
    Clase para representar una nave en el universo de Star Wars.

    Atributos:
    ----------
    mglt : str
        La velocidad en MGLT (Megalight por hora).
    capacidad_de_carga : str
        La capacidad de carga de la nave.
    consumibles : str
        Los consumibles que puede llevar la nave.
    costo_en_créditos : str
        El costo de la nave en créditos.
    creado : str
        La fecha y hora de creación del recurso.
    tripulacion : str
        El número de tripulantes de la nave.
    editado : str
        La fecha y hora de la última edición del recurso.
    calificación_de_hiperimpulsor : str
        La calificación del hiperimpulsor de la nave.
    longitud : str
        La longitud de la nave.
    fabricante : str
        El fabricante de la nave.
    velocidad_atmosférica_máxima : str
        La velocidad máxima de la nave en la atmósfera.
    modelo : str
        El modelo de la nave.
    nombre : str
        El nombre de la nave.
    pasajeros : str
        El número de pasajeros que puede llevar la nave.
    peliculas : list
        Una lista de películas en las que aparece la nave.
    pilotos : list
        Una lista de pilotos que han operado la nave.
    clase_de_nave : str
        La clase de la nave.
    """
    def __init__(self, 
                 mglt : str, 
                 cargo_capacity : str, 
                 consumables : str, 
                 cost_in_credits : str, 
                 created : str, 
                 crew : str, 
                 edited : str, 
                 hyperdrive_rating : str, 
                 length : str, 
                 manufacturer : str,
                 max_atmosphering_speed : str, 
                 model : str, 
                 name : str,
                 passengers : str,
                 films : list,
                 pilots : list,
                 starship_class : str):
        self.mglt = mglt
        self.capacidad_de_carga = cargo_capacity
        self.consumibles = consumables
        self.costo_en_créditos = cost_in_credits
        self.creado = created
        self.tripulacion = crew
        self.editado = edited
        self.calificación_de_hiperimpulsor = hyperdrive_rating
        self.longitud = length
        self.fabricante = manufacturer
        self.velocidad_atmosférica_máxima = max_atmosphering_speed
        self.modelo = model
        self.nombre = name
        self.pasajeros = passengers
        self.peliculas = films
        self.pilotos = pilots
        self.clase_de_nave = starship_class