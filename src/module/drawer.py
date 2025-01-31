import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

class Drawer:
  def __init__(self, df):
    self.df = df
    self.new_df = None
  
  # 方対数グラフを描画する
  def draw(self):
    # magnitudeが3から8の範囲のデータを抽出
    self.new_df = self.df[(self.df['magnitude'] >= 4) & (self.df['magnitude'] <= 7)]

    # xをエネルギー、yを頻度として最小二乗法で回帰直線を求める
    x = np.array(self.new_df['magnitude']).reshape(-1, 1)
    y = np.log10(self.new_df['count'])
    lr = LinearRegression()
    lr.fit(x, y)
    
    print(f'回帰式: y = {lr.coef_[0]:.2f}x + {lr.intercept_:.2f}')

    plt.scatter(self.df['magnitude'], self.df['count'], color='red', marker='o')
    plt.yscale('log')

    # マグニチュードは3から
    plt.xlim(3,10)

    # タイトル・ラベル
    plt.title('Japan Earthquake Magnitude Frequency')
    plt.xlabel('Magnitude')
    plt.ylabel('Frequency')

    # 回帰式も表示

    plt.show()
