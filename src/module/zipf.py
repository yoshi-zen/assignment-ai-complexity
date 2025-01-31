import matplotlib.pyplot as plt

class Zipf:
  def __init__(self, df, column_name):
    self.df = df
    self.column_name = column_name

  def zipf(self):
    # マグニチュードを0.5ごとに集計
    # self.df[self.column_name] = self.df[self.column_name].apply(lambda x: round(x * 2) / 2)
    return self.df.groupby(self.column_name).size().reset_index(name='count')


