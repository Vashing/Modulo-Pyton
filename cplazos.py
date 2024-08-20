class CuentaAhorro:
    def __init__(self):
        self.saldo = 0.0

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return True
        return False

    def mostrar_saldo(self):
        return self.saldo
