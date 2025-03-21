#Cálculo de Descuento en Compras
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento /100)
    return descuento

# Solicitar el monto de la compra al usuario
if __name__ == '__main__':
    monto1 = 2000
    monto2 = 3000

    ##llamada 01
    descuento1 = calcular_descuento(monto1)
    print(f"Monto de la compra es: {monto1}, el descuento es $: {descuento1}")

    ##llamada 02
    porcentaje_descuento = 20
    descuento2 = calcular_descuento(monto2, porcentaje_descuento)
    print(f"Monto de la compra es: {monto2}, el descuento es $: {descuento2} ")

