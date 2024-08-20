from cplazos import CuentaAhorro
import datetime as dt

miCuentaCliente = CuentaAhorro()

pregunta = 0
while pregunta != 4:
    print("MENÚ CUENTA:")
    print("1. Ingresar")
    print("2. Retirar")
    print("3. Mostrar movimientos")
    print("4. Salir")
    pregunta = int(input("Ingrese su opción: "))
    if pregunta != 4:
        if pregunta == 1:
            with open("log.txt", "a") as f:
                cantidad = float(input("Indique la cantidad a ingresar: "))
                if miCuentaCliente.ingresar(cantidad):
                    hoy = dt.datetime.now()
                    fecha1 = hoy.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"Se ingresaron: ${cantidad} a las {fecha1}.\n")
                else:
                    print("La cantidad a ingresar debe ser positiva.")
        elif pregunta == 2:
            with open("log.txt", "a") as f:
                cantidad = float(input("Indique la cantidad a retirar: "))
                if miCuentaCliente.retirar(cantidad):
                    hoy = dt.datetime.now()
                    fecha1 = hoy.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"Se retiraron: ${cantidad} a las {fecha1}.\n")
                else:
                    print("Saldo insuficiente o cantidad inválida.")
        elif pregunta == 3:
            with open("log.txt", "r") as f:
                contenido = f.read()
                print(contenido)
        elif pregunta == 4:
            input("Presione la tecla Enter para Salir: ")
        else:
            print("Opción incorrecta. Inténtelo de nuevo")