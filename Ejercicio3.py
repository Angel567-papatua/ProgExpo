"""
Autor: Moises A. Valle A.
Fecha: 2/06/25
Versión: 1.0
Descripción: Cree un programa que permita llevar un registro de ventas en una feria 
estudiantil organizada por la UAM. La feria se desarrollará durante tres días, con 
cuatro stands por día. Cada stand ofrecerá tres productos distintos. El sistema 
deberá permitir ingresar el monto de venta por producto y mostrar un resumen por 
stand, por día, y un total general de la feria. 
"""

def registroFeria():

    total_general = 0

        for dia in range(1, 4):  # 3 días
        print(f"\n--- Día {dia} ---")
        total_dia = 0

        for stand in range(1, 5):  # 4 stands
        print(f"\nStand {stand}:")
        total_stand = 0

        for producto in range(1, 4):  # 3 productos
            venta = float(input(f"  Ingrese venta del Producto {producto}: C$ "))
            total_stand += venta

        print(f"  Total ventas del Stand {stand}: C$ {total_stand:.2f}")
        total_dia += total_stand

    print(f"\nTotal del Día {dia}: C$ {total_dia:.2f}")
    total_general += total_dia

    print(f"\n=== TOTAL GENERAL DE LA FERIA: C$ {total_general:.2f} ===")
    
registroFeria()