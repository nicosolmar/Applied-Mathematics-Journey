print("Ha pedido comparar las dos opcciones de suscripción.", "\nA: paga $5000 al mes y $2000 por cada serie de HBO que vea.", "\nB: paga $10000 al mes y $1000 por cada serie de HBO que vea." "\nComprobemos cuál es mejor dependiendo de cuántas series adicionales va a comprar.")
x = int(input("Ingrese el número de series adicionales que va a comprar: "))
while x < 0:
  print("Sólo cantidades no negativas.")
  x = int(input("Ingrese el número de series adicionales que va a comprar: "))
else:
  a = 5000 + 2000*x
  b = 10000 + 1000*x
  if a<b:
    print("Te sirve la opción a, que da ", a)
  elif a>b:
    print("Te sirve la opción b, que da ", b)
  while a==b:
    c = int(input("Cualquiera de los dos ofertas es igual. Escribe 1 para escoger la A y 2 para escoger la B: "))
    if c == 1:
      print("Elegiste A. Vale" )
      break
    elif c == 2:
      print("Elegiste B")
      break
    else:
      print("¡A o B!")