# Escribe tú codigo aquí
def funcion_01(a, b):
    suma = a + b 
    return suma

def funcion_02():
    num = int(input("Ingrese un número: "))
    for i in range(num + 1):
        print(i)

def funcion_03():
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("El número", num, "es par.")
    else:
        print("El número", num, "es impar.")

def funcion_04(nombre):
    saludo = f"Hola, {nombre}, ¿cómo estás?"
    return saludo

def funcion_05():
    num = int(input("Ingrese un número: "))
    print(f"Tabla de multiplicar del {num}:")

    for i in range(1, 6):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

def funcion_06():
    edad_str = input("Ingrese su edad: ")
    edad = int(edad_str)  # Convertir el input a entero
    
    if edad < 5:
        print("Eres un bebé")
    elif 5 <= edad <= 12:
        print("Eres un niño")
    elif 13 <= edad <= 19:
        print("Eres un adolescente")
    else:
        print("Eres un adulto")
        