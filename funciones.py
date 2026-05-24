
"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre
específico para realizar una tarea determinada.

Sintaxis:

def nombreFuncion(parametros):
    bloque de instrucciones

nombreFuncion(parametros)

Tipos de funciones:

Funciones tipo "Procedimiento"
1.- No recibe parámetros y no regresa valor
3.- Recibe parámetros y no regresa valor

Funciones tipo "Función"
2.- No recibe parámetros y regresa valor
4.- Recibe parámetros y regresa valor
"""

# 1.- Función que no recibe parámetros y no regresa valor

def saludo():
    print("Hola, bienvenido al programa")

# 3.- Función que recibe parámetros y no regresa valor

def suma(a, b):
    resultado = a + b
    print("La suma es:", resultado)

# 2.- Función que no recibe parámetros y regresa valor

def obtener_nombre():
    nombre = "Luis Alejandro"
    return nombre


# 4.- Función que recibe parámetros y regresa valor

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


# Invocar las funciones

# Función 1
saludo()

# Función 3
suma(5, 10)

# Función 2
nombre_usuario = obtener_nombre()
print("El nombre es:", nombre_usuario)

# Función 4
resultado_multiplicacion = multiplicar(4, 6)
print("La multiplicación es:", resultado_multiplicacion)