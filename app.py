import os
import pandas as pd

from dashboard.dashboard import Dashboard

df_dir = "data"
df_day = pd.read_csv(os.path.join(df_dir, "day.csv"))
df_hour = pd.read_csv(os.path.join(df_dir, "hour.csv"))

if __name__ == '__main__':
    dashboard = Dashboard (df_day, df_hour)
    dashboard.run()