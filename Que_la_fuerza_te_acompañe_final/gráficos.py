import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd
from naves import Nave
from peliculas import Película
from especies import Especie
from planetas import Planeta
from personajes import Personaje

def graficar_personajes_por_planeta(lista_personajes, lista_planetas):
    conteo_personajes = {}
    for personaje in lista_personajes:
        planeta = personaje.planeta_origen
        for planet in lista_planetas:
            if planet.url in planeta:
                planeta_personaje = planet.nombre
                if planeta_personaje in conteo_personajes:
                    conteo_personajes[planeta_personaje] += 1
                else:
                    conteo_personajes[planeta_personaje] = 1

    plt.bar(conteo_personajes.keys(), conteo_personajes.values())
    plt.xlabel('Planeta')
    plt.ylabel('Número de Personajes')
    plt.title('Número de Personajes por Planeta')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Parte de las naves:

def generar_graficos_naves(lista_naves):
    # Filtrar datos válidos y convertir a tipos numéricos
    naves_validas = [nave for nave in lista_naves if nave.longitud and nave.capacidad_de_carga and nave.calificación_de_hiperimpulsor and nave.mglt]
    
    nombres = [nave.nombre for nave in naves_validas]
    longitudes = [float(nave.longitud) for nave in naves_validas if nave.longitud != 'unknown']
    capacidades_de_carga = [float(nave.capacidad_de_carga) for nave in naves_validas if nave.capacidad_de_carga != 'unknown']
    hiperimpulsores = [float(nave.calificación_de_hiperimpulsor) for nave in naves_validas if nave.calificación_de_hiperimpulsor != 'unknown']
    mglt = [float(nave.mglt) for nave in naves_validas if nave.mglt != 'unknown']

    # Gráfico de Longitud de la nave
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, longitudes, color='skyblue')
    plt.xlabel('Longitud (m)')
    plt.title('Longitud de las Naves')
    plt.tight_layout()
    plt.show()

    # Gráfico de Capacidad de carga
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, capacidades_de_carga, color='lightgreen')
    plt.xlabel('Capacidad de Carga (kg)')
    plt.title('Capacidad de Carga de las Naves')
    plt.tight_layout()
    plt.show()

    # Gráfico de Clasificación de hiperimpulsor
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, hiperimpulsores, color='salmon')
    plt.xlabel('Clasificación de Hiperimpulsor')
    plt.title('Clasificación de Hiperimpulsor de las Naves')
    plt.tight_layout()
    plt.show()

    # Gráfico de MGLT
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, mglt, color='violet')
    plt.xlabel('MGLT (Modern Galactic Light Time)')
    plt.title('MGLT de las Naves')
    plt.tight_layout()
    plt.show()

def estadisticas_naves(lista_naves): # Lo voy a dejar así temporalmente 
    naves_df = pd.DataFrame([{
        'Nombre': nave.nombre,
        'Longitud': nave.longitud,
        'Capacidad de carga': nave.capacidad_de_carga,
        'Clasificación de hiperimpulsor': nave.calificación_de_hiperimpulsor
    } for nave in lista_naves])
    
    print("Estadísticas de Naves")
    print(naves_df.describe())