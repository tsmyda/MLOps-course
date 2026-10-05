import joblib
from sklearn.datasets import load_iris

MODEL_PATH = "model.joblib"
CLASS_NAMES = load_iris().target_names


def load_model(path: str = MODEL_PATH):
    return joblib.load(path)


def predict(model, features: dict) -> str:
    X = [
        [
            features["sepal_length"],
            features["sepal_width"],
            features["petal_length"],
            features["petal_width"],
        ]
    ]
    class_idx = model.predict(X)[0]
    return str(CLASS_NAMES[class_idx])
