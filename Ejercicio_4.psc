// Autor: André Guido.
// Fecha: 02/06/2025.
// Versión: 1.0.
// Descripción: Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
// universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
// tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
// generar el promedio semanal correspondiente. 
Algoritmo ConsumoEnergetico
	// Declaración de variables
	Definir dias,turnos Como Caracter
	Definir edificios, edificio, dia, turno Como Entero
	Definir promsemanaledificio, promsemanaltotal, consumo,totaldia,totaledificio Como Real
	
	// Definición de los valores de los arreglos.
	Dimension edificios[4]
	
	Dimension totaledificio[4]
	
	Dimension promsemanaledificio[4]
	
	Dimension dias[7]
	dias[0]=["Lunes"]
	dias[1]=["Martes"]
	dias[2]=["Miércoles"]
	dias[3]=["Jueves"]
	dias[4]=["Viernes"]
	dias[5]=["Sábado"]
	dias[6]=["Domingo"]
	
	Dimension turnos[3]
	turnos[0]=["mañana"]
	turnos[1]=["tarde"]
	turnos[2]=["noche"]
	
	// Inicialización de variables
	edificio=0
	dia=0
	turno=0
	promsemanaltotal=0
	
	// Bucle para entrada de datos.
	Para edificio=0 Hasta 3 Hacer
		Escribir "Edificio #",edificio+1
		totaldia=0
		Para dia=0 Hasta 6 Hacer
			Escribir "",dias[dia]
			Para turno=0 Hasta 2 Hacer
				Escribir "Ingrese el consumo energético del turno de la ",turnos[turno],": "
				Leer consumo
				totaldia=totaldia+consumo
			FinPara
		FinPara
		totaledificio[edificio]=totaldia
		Limpiar Pantalla
	FinPara
	
	// Bucle para mostrar el total por edificio.
	Para edificio=0 Hasta 3 Hacer
		// Operación para obtener el total semanal entre todos los edificios.
		promsemanaltotal=promsemanaltotal+totaledificio[edificio]
		
		// Operación para obtener el promedio semanal de cada edificio.
		promsemanaledificio[edificio]=totaledificio[edificio]/7
		
		// Salida de la información.
		Escribir "El consumo total del edificio #",edificio+1," es: ",totaledificio[edificio]," Kw."
		Escribir "El promedio de consumo semanal del edificio #",edificio+1," es: ",promsemanaledificio[edificio]," Kw."
	FinPara
	
	// Operación para obtener el promedio semanal entre los 4 edificios
	promsemanaltotal=promsemanaltotal/4
	
	// Salida de la información.
	Escribir "El promedio semanal de consumo entre los 4 edificios es de: ",promsemanaltotal," Kw."
FinAlgoritmo
