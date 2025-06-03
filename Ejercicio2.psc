// Autor: Moises A. Valle A.
// Fecha: 2/06/25
// Versión: 1.0
// Descripción: Cree un programa que permita llevar un registro de ventas en una feria 
// estudiantil organizada por la UAM. La feria se desarrollará durante tres días, con 
// cuatro stands por día. Cada stand ofrecerá tres productos distintos. El sistema 
// deberá permitir ingresar el monto de venta por producto y mostrar un resumen por 
// stand, por día, y un total general de la feria. 

Algoritmo resgistroFeria
	Definir dia,stand,producto Como Entero
	Definir total_stand,total_dia,total_general Como Real
	Definir venta Como Real
	
	total_general = 0
	
    Para dia=1 hasta 3 hacer
        Escribir "Día", dia
        total_dia = 0
		
        Para stand=1 hasta 4 hacer
            Escribir "Stand", stand
            total_stand = 0
			
            Para producto=1 hasta 3 hacer
                Escribir "Ingrese venta del Producto", producto
                Leer venta
                total_stand = total_stand + venta
            FinPara
			
            Escribir "Total ventas del Stand", stand, ": C$", total_stand
            total_dia = total_dia + total_stand
        FinPara
		
        Escribir "Total del Día", dia, ": C$", total_dia
        total_general = total_general + total_dia
    FinPara
	
    Escribir "TOTAL GENERAL DE LA FERIA: C$", total_general
FinAlgoritmo
