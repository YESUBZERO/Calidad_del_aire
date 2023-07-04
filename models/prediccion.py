import joblib

def clasificar(pm):
    # Cargar el modelo desde el archivo
    modelo_rf_cargado = joblib.load('models/modelo_rf.pkl')

    # Supongamos que tienes un dato de entrada en forma de lista o arreglo llamado 'dato_entrada'
    # Realizar la predicción con el modelo cargado
    prediccion = modelo_rf_cargado.predict([[pm]])

    # Imprimir la predicción
    print(prediccion[0])

    return prediccion[0]

