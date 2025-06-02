"""
Autor: Marlon Emanuel Aguilar Ortega
Version:1.0
descripcion:Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. 

"""

# Cantidad de secciones que hay en la UAM
secciones = 3

# Cantidad de días que se tomará asistencia
dias = 5

# Cantidad de estudiantes por sección
estudiantes = 6

# Lista para almacenar el total de asistencias de cada sección
# totales_seccion[0] → Sección 1, totales_seccion[1] → Sección 2, etc.
totalesSeccion = [0, 0, 0]

# Variable para contar el total general de asistencias de todas las secciones
totalGeneral = 0

# Bucle principal: recorre cada sección (de la 0 a la 2)
for seccion in range(secciones):
    print("\nRegistro de asistencia - Sección", seccion + 1)  # Sección actual (se suma 1 porque comienza desde 0)
    
    # Segundo bucle: recorre los 5 días de clase
    for dia in range(dias):
        print(" Día", dia + 1)  # Día actual
        
        # Tercer bucle: recorre los 6 estudiantes de la sección en ese día
        for estudiante in range(estudiantes):
            # Se pide al usuario que ingrese si el estudiante asistió o no
            asistencia = int(input("  ¿Asistió el estudiante " + str(estudiante + 1) + "? (1 = Sí, 0 = No): "))
            
            # Si el estudiante asistió (es decir, si se escribió 1), se suman los totales
            if asistencia == 1:
                totalesSeccion[seccion] += 1  # Se suma al total de esa sección
                totalGeneral += 1             # También se suma al total general

# Después de tomar toda la asistencia, mostramos un resumen final

print("\n Resumen de asistencias por sección:")

# Este bucle recorre la lista totales_seccion y muestra el total de cada sección
for seccion in range(secciones):
    print(" Sección", seccion + 1, ":", totalesSeccion[seccion], "asistencias")

# Finalmente, se muestra el total general de la semana
print("\n Total general de asistencias en la semana:", totalGeneral)
