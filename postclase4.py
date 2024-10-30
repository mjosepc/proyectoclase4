import random
import math

# Función para generar un movimiento lineal
def generar_movimiento_lineal(puntos=10, ejemplos=100):
    datos_lineales = []
    for _ in range(ejemplos):
        x_inicial = random.uniform(0, 10)
        y_inicial = random.uniform(0, 10)
        dx = random.uniform(0.5, 1.5)
        dy = random.uniform(0.5, 1.5)
        
        trayectoria = []
        for i in range(puntos):
            x = x_inicial + i * dx
            y = y_inicial + i * dy
            trayectoria.append([x, y])
        datos_lineales.append(trayectoria)
    return datos_lineales

# Función para generar un movimiento circular
def generar_movimiento_circular(puntos=10, ejemplos=100):
    datos_circulares = []
    for _ in range(ejemplos):
        radio = random.uniform(5, 10)
        centro_x = random.uniform(0, 20)
        centro_y = random.uniform(0, 20)
        angulo_inicial = random.uniform(0, 2 * math.pi)
        
        trayectoria = []
        for i in range(puntos):
            angulo = angulo_inicial + i * (2 * math.pi / puntos)
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            trayectoria.append([x, y])
        datos_circulares.append(trayectoria)
    return datos_circulares

# Función para generar un movimiento aleatorio
def generar_movimiento_aleatorio(puntos=10, ejemplos=100):
    datos_aleatorios = []
    for _ in range(ejemplos):
        x, y = random.uniform(0, 10), random.uniform(0, 10)
        trayectoria = []
        for _ in range(puntos):
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            x += dx
            y += dy
            trayectoria.append([x, y])
        datos_aleatorios.append(trayectoria)
    return datos_aleatorios

# Generar los conjuntos de datos
datos_lineales = generar_movimiento_lineal()
datos_circulares = generar_movimiento_circular()
datos_aleatorios = generar_movimiento_aleatorio()

# Ejemplo de visualización de uno de los datos generados
print("Ejemplo de datos de movimiento lineal:", datos_lineales[0])
print("Ejemplo de datos de movimiento circular:", datos_circulares[0])
print("Ejemplo de datos de movimiento aleatorio:", datos_aleatorios[0])
