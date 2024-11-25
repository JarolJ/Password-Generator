import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def guardar_contraseña(nombre, contraseña):
    with open("contraseñas.txt", "a") as archivo:
        archivo.write(f"{nombre}: {contraseña}\n")

def main():
    print("Bienvenido al generador de contraseñas seguras")
    while True:
        try:
            longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8): "))
            if longitud < 8:
                print("La longitud mínima es de 8 caracteres. Inténtelo de nuevo.")
                continue
            nombre = input("Ingrese un nombre para identificar la contraseña: ")
            contraseña = generar_contraseña(longitud)
            guardar_contraseña(nombre, contraseña)
            print(f"Su nueva contraseña segura es: {contraseña}")
            otra = input("¿Desea generar otra contraseña? (s/n): ").lower()
            if otra != 's':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()