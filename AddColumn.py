import pandas as pd
import glob

filepath = r"C:\Index"

for file in glob.glob(filepath + "\*.csv"):

    df = pd.read_csv(file)
    df['Volume'] = '0'
    df['Open Interest'] = '0'
    df['Ticker'] = 'NIFTY'
    ndf=df[['TickerNew','Date', 'Time', 'Open', 'High', 'Low', 'Close','Volume', 'Open Interest']]
    print(file)
    ndf.to_csv(file,index=False)
