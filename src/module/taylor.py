import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

class Taylor:
  def __init__(self, df):
    self.df = df

  def taylor(self):
    # データフレームを半年ごとに分割
    self.df["datetime"] = pd.to_datetime(self.df["date"] + " " + self.df["time"], format="%Y/%m/%d %H:%M:%S.%f")
    self.df["period"] = self.df["datetime"].dt.to_period("6M")

    # ある期間における地震の発生回数を集計
    grouped = self.df.groupby(["period", "magnitude"]).size().reset_index(name="count")

    # 
    summary = grouped.groupby("magnitude")["count"].agg(["mean", "std"]).reset_index()
    summary = summary[(summary["mean"] > 0) & (summary["std"] > 0)]  # Avoid log(0)
    summary["log_mean"] = np.log(summary["mean"])
    summary["log_std"] = np.log(summary["std"])
    
    slope, intercept, r_value, _, _ = linregress(summary["log_mean"], summary["log_std"])
    
    print(f"Taylor's Law: log(std) = {slope:.2f} * log(mean) + {intercept:.2f} (R^2={r_value**2:.2f})")

    plt.scatter(summary["log_mean"], summary["log_std"], label="Data")
    plt.plot(summary["log_mean"], slope * summary["log_mean"] + intercept, color='red', label=f'Taylor Law Fit (Slope={slope:.2f})')
    # M6以上のデータにラベルを付与
    for _, row in summary.iterrows():
        if row["magnitude"] >= 4 and row["magnitude"] <= 6:
            plt.text(row["log_mean"], row["log_std"], f"M{row['magnitude']:.1f}", fontsize=10, ha='right', color='blue')
    
    plt.xlabel("log(Mean Count)")
    plt.ylabel("log(Standard Deviation)")
    plt.legend()
    plt.title("Taylor's Law for Earthquake Magnitude Occurrences")
    plt.show()

  
    
    
    
  
