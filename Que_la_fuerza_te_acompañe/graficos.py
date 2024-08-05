import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd
from naves import Nave
from peliculas import Película
from especies import Especie
from planetas import Planeta
from personajes import Personaje

def graficar_personajes_por_planeta(lista_personajes):
    conteo_personajes = {}
    for personaje in lista_personajes:
        planeta = personaje.planeta_origen
        if planeta in conteo_personajes:
            conteo_personajes[planeta] += 1
        else:
            conteo_personajes[planeta] = 1

    plt.bar(conteo_personajes.keys(), conteo_personajes.values())
    plt.xlabel('Planeta')
    plt.ylabel('Número de Personajes')
    plt.title('Número de Personajes por Planeta')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def graficar_caracteristicas_naves(lista_naves):
    naves_df = pd.DataFrame([{
        'Nombre': nave.nombre,
        'Longitud': nave.longitud,
        'Capacidad de carga': nave.capacidad_de_carga,
        'Clasificación de hiperimpulsor': nave.calificación_de_hiperimpulsor
    } for nave in lista_naves])
    
    naves_df.plot(x='Nombre', y=['Longitud', 'Capacidad de carga'], kind='bar')
    plt.title('Características de las Naves')
    plt.xlabel('Nombre de la Nave')
    plt.ylabel('Valor')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def estadisticas_naves(lista_naves):
    naves_df = pd.DataFrame([{
        'Nombre': nave.nombre,
        'Longitud': nave.longitud,
        'Capacidad de carga': nave.capacidad_de_carga,
        'Clasificación de hiperimpulsor': nave.calificación_de_hiperimpulsor
    } for nave in lista_naves])
    
    print("Estadísticas de Naves")
    print(naves_df.describe())