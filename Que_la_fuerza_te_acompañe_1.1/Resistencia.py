import api
from Jedy import Jedy
from Pelicula import Pelicula
from Planetas import Planetas

class Resistencia:
  def __init__(self) -> None:
    self.lista_personajes=[]
    self.lista_peliculas=[]
    self.lista_planetas=[]

  def start(self):
    self.carga_personaje()
    while True:
      print(""" BIENVENIDO A STAR WARS METROPEDIA
            En un lugar muy muy lejano...
            1. Ver listas
            2. Buscar Personajes
            3. Graficos y Estadisticas
            4. Misiones
            5. Salir
            """)
      opcion = input("¿Qué deseas hacer? ")
      if opcion == "1":
        self.listas()
      elif opcion == "2":
        self.busqueda_personajes()
      elif opcion == "3":
        self.graficos_estadisticas()
      elif opcion == "4":
        self.misiones()
      elif opcion =="5":
        break
      else:
        print("Opcion invalida")

  def carga_personaje(self):
      lista_personajes=[]
      db=api.cargar_api("https://swapi.dev/api/people/")
      for jedy in db:
        lista_personajes.append(Jedy(jedy["name"],jedy["height"],jedy["homeworld"],jedy["films"],jedy["date_of_birth"]))
      for jedy in lista_personajes:
        jedy.show()

  def cargar_peliculas(self):
    listas_peliculas=[]
    db=api.cargar_api("https://swapi.dev/api/films/")
    for pelicula in db:
      listas_peliculas.append(Pelicula(pelicula["title"],pelicula["episode_id"],pelicula["opening_crawl"],pelicula["director"],pelicula["release_date"]))
    for pelicula in listas_peliculas:
      pelicula.show()

  def cargar_planetas(self):
    listas_planetas=[]
    db=api.cargar_api("https://swapi.dev/api/planets/")
    for planeta in db:
      listas_planetas.append(Planetas(planeta["name"],planeta["orbital_period"],planeta["rotation_period"],planeta["population"],planeta["climate"]))
    for planeta in listas_planetas:
      planeta.show()

  def listas(self):
    op=input("""
          1.Lista de Peliculas de la Saga
          2.Lista de Seres Vivos de la Saga
          3.Lista de las especies de seres vivos de la saga
          4.Lista de planetas
          """)
    if op == "1":
      pass
    elif op == "2":
      pass
    elif op == "3":
      pass
    elif op =="4":
      pass
    else:
      print("Opcion invalida")  

  

  def graficos_estadisticas(self):
    op_2=input("""
          1.Gráfico de cantidad de personajes nacidos en cada planeta
          2.Gráficos de características de naves
          3.Estadísticas sobre naves
          """)
    if op_2 == "1":
      pass
    elif op_2 == "2":
      pass
    elif op_2 == "3":
      pass
    else:
      print("Opcion invalida")

  def misiones(self):
    op_3=input("""
          1.Construir misión
          2.Modificar misión
          3.Visualizar misión
          4.Guardar misiones
          5.Cargar misiones
          """)
    if op_3 == "1":
      pass
    elif op_3 == "2":
      pass
    elif op_3 == "3":
      pass
    elif op_3 == "4":
      pass
    elif op_3 == "5":
      pass
    else:
      print("Opcion invalida")

  def busqueda_personajes(self):
    pass