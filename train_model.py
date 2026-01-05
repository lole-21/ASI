from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix, classification_report
from joblib import dump
import os
import json
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn

def main():

    iris = load_iris()
    X, y = iris.data, iris.target


    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=7)


    classifiers = {
        "LogisticRegression": LogisticRegression(max_iter=200),
        "SupportVectorMachine": SVC(),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "K-NearestNeighbors": KNeighborsClassifier(),
        "RandomForest": RandomForestClassifier(random_state=42)
    }


    mlflow.set_experiment("iris-model-zoo")

    best_f1 = 0
    best_model_name = None
    best_model = None
    best_run_id = None

    for name, model in classifiers.items():
        with mlflow.start_run(run_name=name):

            model.fit(X_tr, y_tr)
            y_pred = model.predict(X_te)


            acc = accuracy_score(y_te, y_pred)
            f1 = f1_score(y_te, y_pred, average="macro")
            prec = precision_score(y_te, y_pred, average="macro")
            rec = recall_score(y_te, y_pred, average="macro")


            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("f1_macro", f1)
            mlflow.log_metric("precision", prec)
            mlflow.log_metric("recall", rec)


            cm = confusion_matrix(y_te, y_pred)
            plt.figure(figsize=(5,5))
            plt.imshow(cm, cmap="Blues")
            plt.title(f"{name} Confusion Matrix")
            plt.colorbar()
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            cm_path = f"cm_{name}.png"
            plt.savefig(cm_path)
            plt.close()
            mlflow.log_artifact(cm_path)


            report = classification_report(y_te, y_pred)
            report_path = f"classification_report_{name}.txt"
            with open(report_path, "w") as f:
                f.write(report)
            mlflow.log_artifact(report_path)


            mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="IrisModel")


            if f1 > best_f1:
                best_f1 = f1
                best_model_name = name
                best_model = model
                best_run_id = mlflow.active_run().info.run_id

            print(f"{name} Accuracy: {acc:.2f}, F1: {f1:.2f}")


    os.makedirs("app", exist_ok=True)
    dump(best_model, "app/model.joblib")

    meta = {
        "best_model": best_model_name,
        "metrics": {"accuracy": acc, "f1_macro": best_f1},
        "mlflow_run_id": best_run_id,
        "version": "v1.0.0"
    }

    with open("app/model_meta.json", "w") as f:
        json.dump(meta, f, indent=4)

    print("\nTraining complete.")
    print(f"Best model: {best_model_name}")
    print("Saved app/model.joblib and app/model_meta.json")

if __name__ == "__main__":
    main()
