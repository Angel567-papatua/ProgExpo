"""
Autor: Marlon Emanuel Aguilar Ortega
Version:1.0
descripcion:Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. 

"""
def registrarAsistencia():
    secciones = 3
    dias = 5
    estudiantes = 6
    totalesSeccion = [0, 0, 0]
    totalGeneral = 0

    for seccion in range(secciones):
        print("\nRegistro de asistencia - Sección", seccion + 1)  
    for dia in range(dias):
        print(" Día", dia + 1) 
        
    for estudiante in range(estudiantes):
        asistencia = int(input("  ¿Asistió el estudiante " + str(estudiante + 1) + "? (1 = Sí, 0 = No): "))
            
    if asistencia == 1:
        totalesSeccion[seccion] += 1  
        totalGeneral += 1             


    print("\n Resumen de asistencias por sección:")

    for seccion in range(secciones):
        print(" Sección", seccion + 1, ":", totalesSeccion[seccion], "asistencias")

    print("\n Total general de asistencias en la semana:", totalGeneral)

registrarAsistencia()