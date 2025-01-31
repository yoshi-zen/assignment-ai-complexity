import matplotlib.pyplot as plt
import pandas as pd

class CombDrawer:
  def __init__(self, df):
    self.df = df

  def draw(self):
    print(self.df)
    self.df['datetime'] = pd.to_datetime(self.df['date'] + ' ' + self.df['time'], format='%Y/%m/%d %H:%M:%S.%f')
    # マグニチュードが6より大きいデータを抽出
    # self.df = self.df[self.df['magnitude'] >= 4]

    self.df['earthquake'] = 1

    # 時系列でソート
    self.df = self.df.sort_values('datetime')

    # プロット
    plt.figure(figsize=(12, 4))
    plt.bar(self.df['datetime'], self.df['earthquake'], width=0.1, color='r', label='Earthquake')

    # 軸ラベルとタイトル
    plt.xlabel('Time')
    plt.ylabel('Earthquake (1=Occurred)')
    plt.title('Earthquake Occurrence Over Time')

    # y軸の目盛りを 0 と 1 のみに設定
    plt.yticks([0, 1])

    # x軸のラベルを回転
    plt.xticks(rotation=45)

    # グリッドと凡例
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # 表示
    plt.show()