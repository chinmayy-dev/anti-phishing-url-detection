import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def load_data(path):
    df = pd.read_csv(path)
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y


def train_model(X_train, y_train, model_type="random_forest"):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)
    elif model_type == "random_forest":
        model = RandomForestClassifier(random_state=42)
    else:
        raise ValueError("Invalid model type")

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
    }

    return metrics


def print_metrics(metrics):
    print("\nModel Performance:")
    for key, value in metrics.items():
        print(f"{key.capitalize()}: {value:.4f}")


if __name__ == "__main__":
    X, y = load_data("data/dataset_schema_v1.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train, model_type="random_forest")

    metrics = evaluate_model(model, X_test, y_test)

    print_metrics(metrics)