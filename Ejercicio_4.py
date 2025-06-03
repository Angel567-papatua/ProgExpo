'''
Autor: André Guido.
Fecha: 01/06/2025.
Versión: 1.0.
Descripción: Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
generar el promedio semanal correspondiente.
'''
import os
def ConsumoEnergetico():
    
    # Definición de las listas/variables a utilizar
    dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    edificios=4
    turnos=["mañana", "tarde", "noche"]
    consumototal=[0]*edificios
    promsemanal=0

    # Bucle para recorrer cada edificio
    for edificio in range(edificios):
        print(f"Edificio #{edificio+1}.")
        totaldia=0
        
        # Bucle para recorrer los días
        for dia in dias:
            print("\n")
            print(f"{dia}.")
            
            # Bucle para recorrer los turnos del día
            for turno in turnos:
                consumo=float(input(f"Ingrese el consumo energético del turno de la {turno}: "))
                totaldia=totaldia+consumo
        
        # Lista en la que se almacena el total de la semana por edificio
        consumototal[edificio]=totaldia
        os.system("cls")
    
    # Bucle para mostrar los resultados de cada edificio
    for edificio in range(edificios):

        #Operación para obtener el consumo total de todos los edificios.
        promsemanal+=consumototal[edificio]

        # Salida del resultado
        print(f"El consumo total del edificio #{edificio+1} es: {consumototal[edificio]} KW.")
        print("\n")

    # Operación para obtener el promedio semanal del consumo energético.
    promsemanal=promsemanal/4

    # Salida del resultado.
    print(f"El promedio semanal de consumo entre los 4 edificios es de: {promsemanal} KW.")
