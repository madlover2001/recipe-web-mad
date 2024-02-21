import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("Bienvenido al juego de adivinar el número.")
    print("He pensado en un número entre 1 y 10.")

    while True:
        intento = input("Adivina el número: ")
        
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto, intenta de nuevo.")
        else:
            print(f"¡Correcto! El número era {numero_secreto}.")
            print(f"Lo adivinaste en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivina_el_numero()
