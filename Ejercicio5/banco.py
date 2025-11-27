from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = []
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def buscar_cuenta(self, iban):
        for cuenta in self.cuentas:
            if cuenta.iban == iban:
                print(cuenta)
            else:
                print(None)
    def realizar_transferencias(self, iban_origen, iban_destino, cantidad):
        origen = self.buscar_cuenta(iban_origen)
        destino = self.buscar_cuenta(iban_destino)

        if origen.retirar(cantidad) is None:
            destino.ingresar(cantidad)
            print(f'Se ha realizado correctamente la transferencia de {cantidad:.2f} de {iban_origen} a {iban_destino}')
