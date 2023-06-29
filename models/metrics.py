from prometheus_client import start_http_server, Gauge
import random
import time

# Crear una métrica de tipo Gauge
sensor_metric = Gauge('sensor_data', 'Datos del sensor')

def read_sensor_data():
    # Simular la lectura de datos del sensor
    # Reemplaza esta función con la lógica real de lectura de datos del sensor
    return random.uniform(0, 100)

def collect_sensor_data():
    while True:
        # Leer los datos del sensor
        sensor_value = read_sensor_data()

        # Actualizar la métrica del sensor con el valor actual
        sensor_metric.set(sensor_value)

        # Esperar un intervalo de tiempo antes de leer nuevamente los datos del sensor
        time.sleep(1)

if __name__ == '__main__':
    # Iniciar el servidor HTTP para exponer las métricas de Prometheus
    start_http_server(8000)

    # Iniciar la recolección de datos del sensor
    collect_sensor_data()
