# 1 y 2. Pedir y leer los 3 números
# Usamos int() para que sean enteros como en tu pseudocódigo
A = int(input("Ingresa el primer número (A): "))
B = int(input("Ingresa el segundo número (B): "))
C = int(input("Ingresa el tercer número (C): "))

# 3. Realizar suma
suma = A + B + C

# 4. Sacar promedio
promedio = suma / 3

# 7. Mostrar resultados iniciales
print(f"\nLa suma es: {suma}")
print(f"El promedio es: {promedio}")

# 5 y 6. Comparar números para determinar el mayor
print("El número mayor es:")

if A >= B and A >= C:
    print(A)

if B >= A and B >= C:
    print(B)

if C >= A and C >= B:
    print(C)