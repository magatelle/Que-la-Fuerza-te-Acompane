class Planetas:
 def __init__(self, nombre,período_órbita,período_rotación,habitantes,clima):
  self.nombre = nombre
  self.período_órbita = período_órbita
  self.período_rotación = período_rotación
  self.habitantes=habitantes
  self.clima=clima

 def show(self):
  print(f"Nombre: {self.nombre}")
  print(f"Período de Orbita: {self.período_órbita}")
  print(f"Período de Rotación: {self.período_rotación}")
  print(f"Habitantes: {self.habitantes}")
  print(f"Clima: {self.clima}")