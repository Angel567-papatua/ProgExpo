# ProgExpo
.
'''
Nombre: Ángel A.Lopez C.
Fecha:2/6/2025
Versión: 1.0
Descripción: Implemente un programa que simule el estado de uso de cmputadoras en dos laboratorios del campus. Cada laboratorio contiene cinco filas
de cuatro comptadoras. Por cada computadora se debe registrar si esta ocupada o libre(puede ingresarse manualmente o simularse con valores aleatorios). 
Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.
'''

import random


FILAS = 5
COLUMNAS = 4

def CrearLaboratorio(aleatorio=True):
    # Crea un laboratorio con computadoras ocupadas/libres.
    return [[random.choice(["Ocupada", "Libre"]) if aleatorio else input(f"Ingrese estado (Ocupada/Libre) para computadora en fila {i+1}, columna {j+1}: ") 
             for j in range(COLUMNAS)] for i in range(FILAS)]

def ContarEstado(laboratorio):
    # Cuenta computadoras ocupadas y libres.
    ocupadas = sum(fila.count("Ocupada") for fila in laboratorio)
    libres = sum(fila.count("Libre") for fila in laboratorio)
    return ocupadas, libres

def MostrarLaboratorio(laboratorio, nombre):
    # Muestra el estado del laboratorio.
    print(f"\nEstado del {nombre}:")
    for fila in laboratorio:
        print(" ".join(fila))
    ocupadas, libres = contar_estado(laboratorio)
    print(f"\nTotal en {nombre}: Ocupadas: {ocupadas}, Libres: {libres}")


lab1 = CrearLaboratorio(aleatorio=True)  
lab2 = CrearLaboratorio(aleatorio=True)


LostrarLaboratorio(lab1, "Laboratorio 1")
MostrarLaboratorio(lab2, "Laboratorio 2")
