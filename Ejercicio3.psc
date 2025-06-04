// Autor: Moises A. Valle A.
// Fecha: 2/06/25
// Versión: 1.0
// Descripción: Cree un programa que permita llevar un registro de ventas en una feria 
// estudiantil organizada por la UAM. La feria se desarrollará durante tres días, con 
// cuatro stands por día. Cada stand ofrecerá tres productos distintos. El sistema 
// deberá permitir ingresar el monto de venta por producto y mostrar un resumen por 
// stand, por día, y un total general de la feria. 

Algoritmo registroFeria
    Definir dia, stand, producto Como Entero
    Definir venta Como Real
    Definir total_stand, total_dia Como Real
    Definir total_general Como Real
	
    total_general = 0
	Dimension total_stand[4]
	Dimension total_dia[3]
	
    Para dia = 1 Hasta 3 Hacer
        Escribir "-----------------------------"
        Escribir "DÍA ", dia
        Escribir "-----------------------------"
		
        Para stand = 1 Hasta 4 Hacer
            total_stand[stand] = 0
        FinPara
		
        Para stand = 1 Hasta 4 Hacer
            Escribir "  Stand ", stand
			
            Para producto = 1 Hasta 3 Hacer
                Escribir "    Ingrese venta del Producto ", producto, ":"
                Leer venta
                total_stand[stand] = total_stand[stand] + venta
            FinPara
			
            Escribir "  Total ventas del Stand ", stand, ": C$", total_stand[stand]
        FinPara
		
        total_dia[dia] = 0
        Para stand = 1 Hasta 4 Hacer
            total_dia[dia] = total_dia[dia] + total_stand[stand]
        FinPara
		
        Escribir ">>> Total del Día ", dia, ": C$", total_dia[dia]
        total_general = total_general + total_dia[dia]
    FinPara
	
    Escribir "==============================="
    Escribir "RESUMEN FINAL DE LA FERIA"
    Para dia = 1 Hasta 3 Hacer
        Escribir "  Total del Día ", dia, ": C$", total_dia[dia]
    FinPara
    Escribir "TOTAL GENERAL DE LA FERIA: C$", total_general
    Escribir "==============================="
	
FinAlgoritmo

