"""
Autor: Moises Valle, André Guido, Marlon Aguilar, Angel Lopéz.
Fecha: 2/06/25
Versión: 1.0
Descripción: Cree un programa que permita llevar un registro de ventas en una feria 
estudiantil organizada por la UAM. La feria se desarrollará durante tres días, con 
cuatro stands por día. Cada stand ofrecerá tres productos distintos. El sistema 
deberá permitir ingresar el monto de venta por producto y mostrar un resumen por 
stand, por día, y un total general de la feria. 
"""
def registrarFeria():
    # Inicialización de variables.
    total_general = 0
    total_stand = [0] * 5     # Índices del 1 al 4 (índice 0 no se usa).
    total_dia = [0] * 4       # Índices del 1 al 3 (índice 0 no se usa).

    # Bucle por 3 días.
    for dia in range(1, 4):
        print("-----------------------------")
        print("DÍA", dia)
        print("-----------------------------")
    
        # Bucle para 4 Stand.
        for stand in range(1, 5):
            total_stand[stand] = 0

        # Bucle por stand.
        for stand in range(1, 5):
            print("  Stand", stand)
        
            # Bucle por 3 producto.
            for producto in range(1, 4):
                venta = float(input(f"    Ingrese venta del Producto {producto}: "))
                total_stand[stand] += venta
        
            print(f"  Total ventas del Stand {stand}: C${total_stand[stand]:.2f}")
    
        # Calcular total del día
        total_dia[dia] = 0
        for stand in range(1, 5):
            total_dia[dia] += total_stand[stand]
    
        print(f">>> Total del Día {dia}: C${total_dia[dia]:.2f}")
        total_general += total_dia[dia]

    # Mostrar resumen final
    print("===============================")
    print("RESUMEN FINAL DE LA FERIA")
    for dia in range(1, 4):
        print(f"  Total del Día {dia}: C${total_dia[dia]:.2f}")
    print(f"TOTAL GENERAL DE LA FERIA: C${total_general:.2f}")
    print("===============================")

registrarFeria()
