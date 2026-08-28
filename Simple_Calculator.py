"""
CALCULADORA EN CONSOLA
Aprende · Construye · Practica
"""

import math
import os

# ============ FUNCIONES DE LA CALCULADORA ============

def mostrar_menu():
    """Muestra el menú principal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    print("=" * 40)
    print("       🧮 CALCULADORA PYTHON 🧮")
    print("=" * 40)
    print("  1.  Suma")
    print("  2.  Resta")
    print("  3.  Multiplicación")
    print("  4.  División")
    print("  5.  División Exacta (//)")
    print("  6.  Módulo (%)")
    print("  7.  Potencia")
    print("  8.  Raíz Cuadrada")
    print("  9.  Seno (en grados)")
    print(" 10.  Coseno (en grados)")
    print(" 11.  Tangente (en grados)")
    print(" 12.  Logaritmo Natural")
    print(" 13.  Historial")
    print("  0.  Salir")
    print("=" * 40)

def obtener_numero(mensaje):
    """Solicita un número al usuario con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingresa un número válido.")

def obtener_operador():
    """Solicita un operador para operaciones binarias."""
    operadores = ['+', '-', '*', '/', '//', '%', '**']
    while True:
        op = input("Operador (+ - * / // % **): ").strip()
        if op in operadores:
            return op
        print("❌ Operador no válido.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("❌ No se puede dividir entre cero.")
    return a / b

def division_exacta(a, b):
    if b == 0:
        raise ValueError("❌ No se puede dividir entre cero.")
    return a // b

def modulo(a, b):
    if b == 0:
        raise ValueError("❌ No se puede dividir entre cero.")
    return a % b

def potencia(a: int, b: int) -> int:
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("❌ No se puede calcular raíz de un número negativo.")
    return math.sqrt(a)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def log_natural(a):
    if a <= 0:
        raise ValueError("❌ El logaritmo solo está definido para números positivos.")
    return math.log(a)

# ============ FUNCIÓN PRINCIPAL ============

def main():
    """Función principal de la calculadora."""
    historial = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '0':
            print("\n👋 ¡Hasta luego!")
            break
        
        # ===== OPERACIONES =====
        try:
            if opcion == '1':  # Suma
                print("\n📌 SUMA")
                a = obtener_numero("Primer número: ")
                b = obtener_numero("Segundo número: ")
                resultado = suma(a, b)
                operacion = f"{a} + {b} = {resultado}"
                
            elif opcion == '2':  # Resta
                print("\n📌 RESTA")
                a = obtener_numero("Primer número: ")
                b = obtener_numero("Segundo número: ")
                resultado = resta(a, b)
                operacion = f"{a} - {b} = {resultado}"
                
            elif opcion == '3':  # Multiplicación
                print("\n📌 MULTIPLICACIÓN")
                a = obtener_numero("Primer número: ")
                b = obtener_numero("Segundo número: ")
                resultado = multiplicacion(a, b)
                operacion = f"{a} × {b} = {resultado}"
                
            elif opcion == '4':  # División
                print("\n📌 DIVISIÓN")
                a = obtener_numero("Dividendo: ")
                b = obtener_numero("Divisor: ")
                resultado = division(a, b)
                operacion = f"{a} ÷ {b} = {resultado}"
                
            elif opcion == '5':  # División Exacta
                print("\n📌 DIVISIÓN EXACTA")
                a = obtener_numero("Dividendo: ")
                b = obtener_numero("Divisor: ")
                resultado = division_exacta(a, b)
                operacion = f"{a} // {b} = {resultado}"
                
            elif opcion == '6':  # Módulo
                print("\n📌 MÓDULO")
                a = obtener_numero("Primer número: ")
                b = obtener_numero("Segundo número: ")
                resultado = modulo(a, b)
                operacion = f"{a} % {b} = {resultado}"
                
            elif opcion == '7':  # Potencia
                print("\n📌 POTENCIA")
                a = obtener_numero("Base: ")
                b = obtener_numero("Exponente: ")
                resultado = potencia(a, b)
                operacion = f"{a} ** {b} = {resultado}"
                
            elif opcion == '8':  # Raíz Cuadrada
                print("\n📌 RAÍZ CUADRADA")
                a = obtener_numero("Número: ")
                resultado = raiz_cuadrada(a)
                operacion = f"√{a} = {resultado}"
                
            elif opcion == '9':  # Seno
                print("\n📌 SENO")
                a = obtener_numero("Ángulo (grados): ")
                resultado = seno(a)
                operacion = f"sen({a}°) = {resultado}"
                
            elif opcion == '10':  # Coseno
                print("\n📌 COSENO")
                a = obtener_numero("Ángulo (grados): ")
                resultado = coseno(a)
                operacion = f"cos({a}°) = {resultado}"
                
            elif opcion == '11':  # Tangente
                print("\n📌 TANGENTE")
                a = obtener_numero("Ángulo (grados): ")
                resultado = tangente(a)
                operacion = f"tan({a}°) = {resultado}"
                
            elif opcion == '12':  # Logaritmo Natural
                print("\n📌 LOGARITMO NATURAL")
                a = obtener_numero("Número (positivo): ")
                resultado = log_natural(a)
                operacion = f"ln({a}) = {resultado}"
                
            elif opcion == '13':  # Historial
                print("\n📋 HISTORIAL")
                if not historial:
                    print("   (Sin operaciones registradas)")
                else:
                    for i, h in enumerate(historial, 1):
                        print(f"   {i}. {h}")
                input("\nPresiona Enter para continuar...")
                continue
                
            else:
                print("❌ Opción no válida.")
                input("Presiona Enter para continuar...")
                continue
            
            # ===== MOSTRAR RESULTADO =====
            print(f"\n✅ RESULTADO: {operacion}")
            historial.append(operacion)  # Guardar en historial
            
            # Preguntar si quiere continuar o salir
            print("\n" + "-" * 40)
            continuar = input("¿Hacer otra operación? (s/n): ").strip().lower()
            if continuar != 's':
                print("\n👋 ¡Hasta luego!")
                break
                
        except ValueError as e:
            print(f"\n{e}")
            input("Presiona Enter para continuar...")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("Presiona Enter para continuar...")

# ============ PUNTO DE ENTRADA ============

if __name__ == "__main__":
    main()