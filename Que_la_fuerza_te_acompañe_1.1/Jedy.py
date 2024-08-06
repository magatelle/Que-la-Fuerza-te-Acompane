class Seres_vivos:
  def __init__(self,nombre,altura,clasificacion,planeta_origen,lenguaje,personajes,episodios):
    self.nombre = nombre
    self.altura=altura
    self.clasificacion=clasificacion
    self.planeta_origen=planeta_origen
    self.lenguaje=lenguaje
    self.personajes=personajes
    self.episodios=episodios

  def show(self):
    print(f"Nombre: {self.nombre}")
    print(f"Altura: {self.altura}")
    print(f"Clasificacion: {self.clasificacion}")
    print(f"Planeta Origen: {self.planeta_origen}")
    print(f"Lenguaje: {self.lenguaje}")
    print(f"Personajes: {self.personajes}")
    print(f"Episodios: {self.episodios}")

class Jedy(Seres_vivos):
 def __init__(self,nombre,gender,planeta_origen):
  self.nombre = nombre
  self.gender = gender
  self.especie = "Humano"
  self.planeta_origen = planeta_origen

 def show(self):
  print(f"Nombre: {self.nombre}")
  print(f"Gender: {self.gender}")
  print(f"Especie: {self.especie}")
  print(f"Planeta Origen: {self.planeta_origen}")

