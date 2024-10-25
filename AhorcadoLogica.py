from ahorcado_graficos import mostrar_ahorcado
from ahorcado_palabras import seleccionar_palabra

# Función para inicializar el estado del juego
def inicializar_juego(palabra_secreta):
    return ["_"] * len(palabra_secreta), set(), set(palabra_secreta), 6

# Función para mostrar el estado actual del juego
def mostrar_estado(palabra_mostrada, intentos_restantes):
    print("\nPalabra: " + " ".join(palabra_mostrada))
    print(f"Te quedan {intentos_restantes} intentos.")
    mostrar_ahorcado(6 - intentos_restantes)

# Función para procesar la letra ingresada por el usuario
def procesar_adivinanza(letra, letras_adivinadas, letras_correctas, palabra_secreta, palabra_mostrada):
    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra. Prueba otra.")
        return False, False

    letras_adivinadas.add(letra)

    if letra in letras_correctas:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        for i, letra_palabra in enumerate(palabra_secreta):
            if letra_palabra == letra:
                palabra_mostrada[i] = letra
        return True, True
    else:
        print(f"Lo siento, la letra '{letra}' no está en la palabra.")
        return True, False

# Función principal del juego
def JuegoAhorcado():
    palabra_secreta = seleccionar_palabra()
    palabra_mostrada, letras_adivinadas, letras_correctas, intentos_restantes = inicializar_juego(palabra_secreta)

    print("¡Bienvenido al juego del ahorcado!")

    while intentos_restantes > 0 and "_" in palabra_mostrada:
        mostrar_estado(palabra_mostrada, intentos_restantes)

        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        valido, acierto = procesar_adivinanza(letra, letras_adivinadas, letras_correctas, palabra_secreta, palabra_mostrada)

        if valido and not acierto:
            intentos_restantes -= 1

    if "_" not in palabra_mostrada:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("\n¡Te has quedado sin intentos! La palabra era:", palabra_secreta)
    mostrar_ahorcado(6 - intentos_restantes)