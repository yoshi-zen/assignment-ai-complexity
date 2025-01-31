# 最小二乗法による傾きを求める
import numpy as np

class LinearRegression:
  def __init__(self):
    self.a = 0
    self.b = 0

  def fit(self, x, y):
    self.a = np.dot(x, y) / np.dot(x, x)
    self.b = np.mean(y) - self.a * np.mean(x)

  def predict(self, x):
    return self.a * x + self.b

  def score(self, x, y):
    y_pred = self.predict(x)
    return 1 - np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2)