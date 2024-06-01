import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def train_model():
    df = pd.read_csv('/data/processed_iris.csv')
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    with open('/models/iris_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # Evaluate model
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))

if __name__ == "__main__":
    train_model()
