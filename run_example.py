# Импорт необходимых библиотек
import mlflow
import os
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Загрузка датасета Diabetes из scikit-learn
df = load_diabetes()

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(df.data, df.target)

# Установка URI для отслеживания MLflow с использованием переменной окружения
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

# Установка имени эксперимента в MLflow
mlflow.set_experiment('Example Project')

# # Включение автоматического логирования параметров и метрик MLflow
mlflow.autolog()

print('Starting...')

# Создание нового run в рамках эксперимента в MLflow
with mlflow.start_run():
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)
    prediction = rf.predict(X_test)
    # Явное логирование метрик
    mlflow.log_metric("my_metric", 0) 

print('The experiment was successfully completed')

