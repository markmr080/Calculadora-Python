import sys

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <numero1> <numero2>")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        resultado = multiplicar(num1, num2)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Los argumentos deben ser números.")
        sys.exit(1)
