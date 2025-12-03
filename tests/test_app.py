import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.predict import pred, CLASS_NAMES

def test_pred_returns_valid_class():
    sample = [5.1, 3.5, 1.4, 0.2]
    result = pred(sample)
    assert result in CLASS_NAMES