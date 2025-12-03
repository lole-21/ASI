import joblib
import numpy as np
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__),"model.joblib")
m = joblib.load(MODEL_PATH)
CLASS_NAMES = ["setosa","versicolor","virginica"]
def pred(feat):
    features = np.array(feat).reshape(1,-1)
    pred = m.predict(features)[0]
    return CLASS_NAMES[pred]