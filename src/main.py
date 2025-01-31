from module.csv_reader import CsvReader
from module.zipf import Zipf
from module.drawer import Drawer
from module.comb_drawer import CombDrawer
from module.taylor import Taylor

import pandas as pd

def main():
  # csvファイルパス
  path = 'data/earthquake.csv'

  # csvファイルを読み込む
  csv_reader = CsvReader()
  df = csv_reader.read(path)

  # マグニチュードが「不明」の行を削除
  df = df[df['magnitude'] != '不明']

  # マグニチュードの方をfloat型に変換
  df['magnitude'] = df['magnitude'].astype(float)

  # マグニチュードを実際のエネルギーに変換
  df['magnitude_energy'] = df['magnitude'].apply(lambda x: 10 ** (1.5 * x + 4.8))

  # マグニチュードごとに回数を集計して両対数グラフ描画を実行
  zipf = Zipf(df, 'magnitude')
  zipf_df = zipf.zipf()

  # 描画
  # drawer = Drawer(zipf_df)
  # drawer.draw()

  # 組み合わせグラフ描画
  # comb_drawer = CombDrawer(df)
  # comb_drawer.draw()

  taylor = Taylor(df)
  taylor.taylor()


if __name__ == '__main__':
  main()