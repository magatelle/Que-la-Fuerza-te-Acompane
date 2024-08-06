class Pelicula:
 def __init__(self,title,episode_id,opening_crawl,director,release_date) -> None:
  self.title = title
  self.episode_id = episode_id
  self.opening_crawl = opening_crawl
  self.director=director
  self.release_date=release_date

 def show(self):
  print(f"Título: {self.title}")
  print(f"Número del episodio {self.episode_id}")
  print(f"Fecha de lanzamiento: {self.release_date}")
  print(f"Apertura del episodio: {self.opening_crawl}")
  print(f"Nombre Director {self.director}")
