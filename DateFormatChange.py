import datetime

import pandas as pd
import glob

filepath = r"D:\ALL Nifty GFDL\Index\onefileindex"

for file in glob.glob(filepath + "\*.csv"):

    df = pd.read_csv(file)
    # df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
   
    print(file)
    df.to_csv(file,index=False)