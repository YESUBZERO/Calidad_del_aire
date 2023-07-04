import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#import matplotlib.pyplot as plt
from sklearn import tree
import joblib

# Cargar los datos
data = pd.read_csv('datasets/data_pm.csv')

# Seleccionar las características y la variable de respuesta
X = data[['PM2.5 AQI']]
y_pm = data['PM2.5 AQI CAT']

label_encoder = {'GOOD': 'BUENA', 'SATISFACTORY': 'SATISFACTORIA', 'MODERATE': 'MODERADA', 'POOR': 'MALA'}
y = y_pm.map(label_encoder)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_pm, test_size=0.2, random_state=42)

# Crear el modelo de Random Forest y ajustarlo a los datos de entrenamiento
model = RandomForestClassifier(n_estimators=100,criterion='entropy', max_features='sqrt', bootstrap=True, max_samples=2/3, oob_score=True, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba y calcular la precisión del modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Precisión:', accuracy)

# Guardar el modelo en un archivo
joblib.dump(model, 'modelo_rf.pkl')