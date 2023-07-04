def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero. Ingrese un valor mayor a cero."

print("Pycalc")
print("Operaciones disponibles con 2 valores:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Selecciona una opcion de operación del 1 al 4 (1/2/3/4): ")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operacion == "1":
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)
elif operacion == "2":
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)
elif operacion == "3":
    resultado = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "4":
    resultado = division(num1, num2)
    print("El resultado de la división es:", resultado)
else:
    print("Operación inválida. Por favor, selecciona una opción válida del 1 al 4 (1/2/3/4).")
