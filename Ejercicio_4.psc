Algoritmo ConsumoEnergetico
	
	// Declaraci�n de variables
	Definir dias,turnos Como Caracter
	Definir edificios, edificio, dia, turno Como Entero
	Definir promsemanaledificio, promsemanaltotal, totalturno Como Real
	
	// Definici�n de los valores de los arreglos.
	Dimension edificios[4]
	
	Dimension dias[7]
	dias[1]=["Lunes"]
	dias[2]=["Martes"]
	dias[3]=["Mi�rcoles"]
	dias[4]=["Jueves"]
	dias[5]=["Viernes"]
	dias[6]=["S�bado"]
	dias[7]=["Domingo"]
	
	Dimension turnos[3]
	turnos[1]=["ma�ana"]
	turnos[2]=["tarde"]
	turnos[3]=["noche"]
	
	// Inicializaci�n de variables
	edificio=0
	dia=0
	turno=0
	promsemanaledificio=0.0
	promsemanaltotal=0.0
	
	// Bucle para entrada de datos.
	Para edificio=0 Hasta 4 Hacer
		Escribir "",edificios[edificio+1]
		Para dia=0 Hasta 7 Hacer
			Escribir "",dias[dia+1]
			Para turno=0 Hasta 3 Hacer
				Escribir "Ingrese el consumo energ�tico del turno de la ",turnos[turno],": "
				Leer totalturno
			FinPara
		FinPara
	FinPara
	
FinAlgoritmo
