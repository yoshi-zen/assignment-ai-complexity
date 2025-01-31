import pandas as pd

# csvファイルを読み込んで、データフレームを返すような責務を持つクラス
class CsvReader:
    def read(self, path):
        return pd.read_csv(path)



    