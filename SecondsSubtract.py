import pandas as pd
import glob


filepath = r"D:\folder"

for file in glob.glob(filepath + "\*.csv"):
    df = pd.read_csv(file, parse_dates=['Date'], dayfirst = True)
    df['Time'] = pd.to_datetime(df['Time'].astype(str)) - pd.DateOffset(hours=0, minutes=0, seconds=59)
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    df.to_csv(file,index=False)
    print(file)

