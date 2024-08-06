import requests as rq

def cargar_api(link):
 info=rq.get(link).json()
 return info
