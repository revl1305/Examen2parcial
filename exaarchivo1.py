import random

# Lista de palabras para adivinar
palabras = ["gato", "perro", "elefante", "leon", "tigre", "jirafa", "rinoceronte", "hormiga", "araña", "avispa"]

def obtener_palabra_aleatoria():
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos = 6  # Número de intentos antes de perder

    print("¡Bienvenido al juego del Ahorcado!")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("\nIntentos restantes:", intentos)
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("¡Ya has intentado esa letra!")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            print("¡Incorrecto!")
            intentos -= 1

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            print("La palabra era:", palabra_secreta)
            break

    if intentos == 0:
        print("\n¡Oh no! Te has quedado sin intentos.")
        print("La palabra era:", palabra_secreta)

if __name__ == "__main__":
    ahorcado()
