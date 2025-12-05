import joblib
import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    print("Loading Iris dataset...")
    iris = load_iris()

    # Création du DataFrame avec EXACTEMENT les noms de ton API
    df = pd.DataFrame(
        iris.data,
        columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ],
    )
    df["target"] = iris.target

    X = df[
        ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    ]
    y = df["target"]

    print("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {acc:.4f}")

    print("Saving model as model.pkl ...")
    os.makedirs("server", exist_ok=True)
    joblib.dump(model, "server/model.pkl")

    print("Model successfully saved at: server/model.pkl")


if __name__ == "__main__":
    main()
