secret_number = 777
number = int()

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

while number != secret_number:
    number = int(input("\n¿Cuál es el número secreto? "))
    if number == secret_number:
            print("\n",secret_number,"¡Bien hecho, muggle! Eres libre ahora.")
    else:
        print("\n¡Ja, ja! ¡Estás atrapado en mi bucle!")   