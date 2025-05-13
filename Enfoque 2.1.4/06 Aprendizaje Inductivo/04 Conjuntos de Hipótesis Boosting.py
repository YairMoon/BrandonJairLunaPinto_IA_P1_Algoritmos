# Boosting con un modelo de clasificación (usamos AdaBoost)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Generamos un dataset de ejemplo
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Creamos un clasificador base (árbol de decisión simple)
clasificador_base = DecisionTreeClassifier(max_depth=1)

# Creamos el modelo AdaBoost
modelo_boosting = AdaBoostClassifier(base_estimator=clasificador_base, n_estimators=50)

# Entrenamos el modelo
modelo_boosting.fit(X, y)

# Realizamos predicciones
predicciones = modelo_boosting.predict(X)
print("Predicciones Boosting:", predicciones)
