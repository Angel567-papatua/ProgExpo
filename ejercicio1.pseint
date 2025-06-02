//Autor: Marlon Emanuel Aguilar.
//Version: 1.0
//descripciondescripcion:Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
//la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
//sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
//sección, así como el total general de la semana. 
Algoritmo  registrarAsistencia
    Definir secciones, dias, estudiantes Como Entero
    Definir totalesSeccion1, totalesSeccion2, totalesSeccion3 Como Entero
    Definir totalGeneral, asistencia Como Entero
    Definir seccion, dia, estudiante Como Entero
	
    secciones <- 3
    dias <- 5
    estudiantes <- 6
    totalGeneral <- 0
    totalesSeccion1 <- 0
    totalesSeccion2 <- 0
    totalesSeccion3 <- 0
	
    Para seccion <- 1 Hasta secciones Hacer
        Escribir ""
        Escribir "Registro de asistencia - Sección ", seccion
		
        Para dia <- 1 Hasta dias Hacer
            Escribir " Día ", dia
			
            Para estudiante <- 1 Hasta estudiantes Hacer
                Escribir "  ¿Asistió el estudiante ", estudiante, "? (1 = Sí, 0 = No): "
                Leer asistencia
				
                Si asistencia = 1 Entonces
                    Si seccion = 1 Entonces
                        totalesSeccion1 <- totalesSeccion1 + 1
                    Sino
                        Si seccion = 2 Entonces
                            totalesSeccion2 <- totalesSeccion2 + 1
                        Sino
                            totalesSeccion3 <- totalesSeccion3 + 1
                        FinSi
                    FinSi
                    totalGeneral <- totalGeneral + 1
                FinSi
            FinPara
        FinPara
    FinPara
	
    Escribir ""
    Escribir "Resumen de asistencias por sección:"
    Escribir " Sección 1: ", totalesSeccion1, " asistencias"
    Escribir " Sección 2: ", totalesSeccion2, " asistencias"
    Escribir " Sección 3: ", totalesSeccion3, " asistencias"
	
    Escribir ""
    Escribir "Total general de asistencias en la semana: ", totalGeneral
FinAlgoritmo

