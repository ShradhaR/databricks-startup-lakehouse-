import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Autolog automatically captures metrics, parameters, and models
mlflow.autolog()

# Fetch features from our Gold Delta Table
dataset = spark.table("gold_user_features").toPandas()

# Create dummy target for classification (e.g., Will Churn?)
dataset['churn'] = [1, 0, 1] # Matching our 3 dummy rows

X = dataset[['total_spend']]
y = dataset['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run(run_name="Churn_Prediction_Startup"):
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X_train, y_train)
    
    predictions = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    # Log custom metric manually if desired
    mlflow.log_metric("custom_accuracy", accuracy)
