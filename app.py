from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['sensor_data']
collection = db['pms7003_data']

@app.route('/data', methods=['POST'])
def almacenar_datos():
    data = request.json
    data['fecha'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    collection.insert_one(data)
    return 'Datos almacenados'

@app.route('/datos_almacenados', methods=['GET'])
def obtener_ultimos_datos():
    #fecha_desde = datetime.now() - timedelta(minutes=33)
    documents = collection.find()
    
    datos = []
    #convertir el _id del documento mongoDB a String
    for document in documents:
        document['_id'] = str(document['_id'])
        datos.append(document)

    #devuelve el JSON consultado a mongoDB
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug = True, host='192.168.0.10', port=5000)