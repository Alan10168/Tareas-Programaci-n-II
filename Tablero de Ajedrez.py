import datetime

# 1. Capturar y mostrar la fecha y hora de inicio
inicio = datetime.datetime.now()
print(f"Proceso iniciado el: {inicio.strftime('%d/%m/%Y %H:%M:%S')}")
print("-" * 40)

# 2. Bucle para calcular las potencias de 2
# Usamos range(65) porque el límite superior no se incluye (llega hasta 64)
for i in range(65):
    resultado = 2**i
    print(f"2 elevado a la {i} = {resultado}")

print("-" * 40)

# 3. Capturar y mostrar la fecha y hora de finalización
fin = datetime.datetime.now()
print(f"Proceso finalizado el: {fin.strftime('%d/%m/%Y %H:%M:%S')}")

# Cálculo opcional del tiempo transcurrido
duracion = fin - inicio
print(f"Tiempo total de ejecución: {duracion.total_seconds()} segundos")