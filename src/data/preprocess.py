import pandas as pd
from sklearn.datasets import load_iris

def preprocess_data():
    data = load_iris()
    df = pd.DataFrame(data=data.data, columns=data.feature_names)
    df['target'] = data.target
    df.to_csv('/data/processed_iris.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
