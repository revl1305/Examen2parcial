import random

# Tamaño del laberinto
filas = 10
columnas = 10

# Símbolos para representar el laberinto
pared = "#"
camino = " "
inicio = "S"
fin = "F"
jugador = "X"

# Crear el laberinto
def crear_laberinto():
    laberinto = [[pared] * columnas for _ in range(filas)]

    # Establecer punto de inicio y final
    laberinto[0][0] = inicio
    laberinto[filas - 1][columnas - 1] = fin

    # Crear caminos
    for i in range(filas * columnas // 3):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        laberinto[fila][columna] = camino

    return laberinto

# Imprimir el laberinto
def imprimir_laberinto(laberinto, jugador_fila, jugador_columna):
    for i in range(filas):
        for j in range(columnas):
            if i == jugador_fila and j == jugador_columna:
                print(jugador, end=" ")
            else:
                print(laberinto[i][j], end=" ")
        print()

# Mover al jugador
def mover_jugador(laberinto, direccion, jugador_fila, jugador_columna):
    nueva_fila = jugador_fila
    nueva_columna = jugador_columna

    if direccion == "w" and jugador_fila > 0 and laberinto[jugador_fila - 1][jugador_columna] != pared:
        nueva_fila -= 1
    elif direccion == "s" and jugador_fila < filas - 1 and laberinto[jugador_fila + 1][jugador_columna] != pared:
        nueva_fila += 1
    elif direccion == "a" and jugador_columna > 0 and laberinto[jugador_fila][jugador_columna - 1] != pared:
        nueva_columna -= 1
    elif direccion == "d" and jugador_columna < columnas - 1 and laberinto[jugador_fila][jugador_columna + 1] != pared:
        nueva_columna += 1

    return nueva_fila, nueva_columna

# Juego principal
def laberinto():
    laberinto_actual = crear_laberinto()
    jugador_fila, jugador_columna = 0, 0

    while True:
        imprimir_laberinto(laberinto_actual, jugador_fila, jugador_columna)

        if jugador_fila == filas - 1 and jugador_columna == columnas - 1:
            print("¡Felicidades, has ganado!")
            break

        movimiento = input("Mueve al jugador (w/a/s/d): ")

        jugador_fila, jugador_columna = mover_jugador(laberinto_actual, movimiento, jugador_fila, jugador_columna)

if __name__ == "__main__":
    laberinto()
