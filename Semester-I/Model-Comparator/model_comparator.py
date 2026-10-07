import numpy as np
import matplotlib.pyplot as plt
print("Ha pedido comparar las dos opcciones de suscripción.", "\nA: paga $5000 al mes y $2000 por cada serie de HBO que vea.", "\nB: paga $10000 al mes y $1000 por cada serie de HBO que vea." "\nComprobemos cuál es mejor dependiendo de cuántas series adicionales va a comprar.")
z = int(input("Ingrese el número de series adicionales que va a comprar: "))
while z < 0:
  print("Sólo cantidades no negativas.")
  z = int(input("Ingrese correctamente el número de series adicionales que va a comprar: "))
else:
  a = 5000 + 2000*z
  b = 10000 + 1000*z
  if a<b:
    print(f'Te sirve la opción A, que da {a}.', '\nMira cómo es la gráfica de las opciones :3')
    x = np.linspace(0,z+1,500)
    grafica_a = 5000 + 2000*x
    grafica_b = 10000 + 1000*x
    fig, ax = plt.subplots()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.plot(x, grafica_a, label="Opción A")
    ax.plot(x, grafica_b, label="Opción B")
    ax.scatter(z, a)
    ax.scatter(z, b)
    ax.annotate(f"A({z}) = {a}", (z, a))
    ax.annotate(f"B({z}) = {b}", (z, b))
    ax.legend()
    ax.grid(True)
    plt.show()
  elif a>b:
    print(f'Te sirve la opción B, que da {b}.', '\nMira cómo es la gráfica de las opciones :3')
    x = np.linspace(0,z+1,500)
    grafica_a = 5000 + 2000*x
    grafica_b = 10000 + 1000*x
    fig, ax = plt.subplots()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.plot(x, grafica_a, label="Opción A")
    ax.plot(x, grafica_b, label="Opción B")
    ax.scatter(z, a)
    ax.scatter(z, b)
    ax.annotate(f"A({z}) = {a}", (z, a))
    ax.annotate(f"B({z}) = {b}", (z, b))
    ax.legend()
    ax.grid(True)
    plt.show()
  while a==b:
    print("Mira, en el punto de intersección de las gráficas :0")
    x = np.linspace(0,z+1,500)
    grafica_a = 5000 + 2000*x
    grafica_b = 10000 + 1000*x
    fig, ax = plt.subplots()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.plot(x, grafica_a, label="Opción A")
    ax.plot(x, grafica_b, label="Opción B")
    ax.scatter(z, a)
    ax.scatter(z, b)
    ax.annotate(f"A({z}) = {a}", (z, a))
    ax.annotate(f"B({z}) = {b}", (z, b))
    ax.legend()
    ax.grid(True)
    plt.show()
    c = int(input("Cualquiera de los dos ofertas es igual. Escribe 1 para escoger la A y 2 para escoger la B: "))
    if c == 1:
      print("Elegiste A. Vale" )
      break
    elif c == 2:
      print("Elegiste B")
      break
    else:
      print("¡A o B!")