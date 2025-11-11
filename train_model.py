from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
import os
def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.3, random_state=7
    )
    classifiers = {
        "LogisticRegression": LogisticRegression(max_iter=200),
        "SupportVectorMachine": SVC(),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "K-NearestNeighbors": KNeighborsClassifier(),
        "RandomForest": RandomForestClassifier(random_state=42)
    }
    results = {}
    for name, model in classifiers.items():
        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_te)
        acc = accuracy_score(y_te, y_pred)
        results[name] = acc
        print(f"{name} Accuracy: {acc:.2f}")

    bestName = max(results, key=results.get)
    best = classifiers[bestName]
    print("\nBest Model:", bestName)

    os.makedirs("app", exist_ok=True)
    path = os.path.join("app", "model.joblib")
    dump(best, path)

    print(f"Model saved to: {path}")
if __name__ == "__main__":
    main()