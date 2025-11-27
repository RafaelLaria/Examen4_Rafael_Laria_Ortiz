from banco import Banco
from cuenta import Cuenta

b = Banco()
c1 = Cuenta('Paco', 'ES66123456789')
c2 = Cuenta('Eva', 'ES660987654321')

b.agregar_cuenta(c1)
b.agregar_cuenta(c2)

c1.ingresar(200)

b.realizar_transferencias('ES66123456789', 'ES660987654321', 50)

print(c1)
print(c2)