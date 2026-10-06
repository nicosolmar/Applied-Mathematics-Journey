
print("Va a adquirir un plan de entretenimiento tal que:", "\nLa suscripción mensual cuesta 5000 y pagará 2000 por cada serie adicional de HBO que vea.", "\nEntonces, ")
x=int(input("¿Cuántas series adicionales va a comprar? "))
while x<=0:
  print("¡Sólo cantidades no negativas!")
  x=int(input("¿Cuántas series adicionales va a comprar? "))
else:
  suscripcion=5000+(2000*x)
  print("La suscripción total cuesta ", suscripcion)