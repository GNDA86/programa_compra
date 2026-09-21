def calcular_total(precio, cantidad):
    total = precio *cantidad
    return total
producto = input("ingrese el nombre del producto: ")
precio = float(input("ingrese el precio unitario: $"))
cantidad = int(input("ingrese la cantidad: "))
total_compra = calcular_total(precio, cantidad)
print("\n------ resumen de la compra ------")
print ("producto:", producto)
print("precio unitario: $", round(precio,2))
print("Cantidad: ", cantidad)
print("Total a pagar: $", round(total_compra,2))
