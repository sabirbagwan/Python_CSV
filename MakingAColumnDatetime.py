import pandas as pd
import glob

file = r"E:\Expiry.csv"

# for file in glob.glob(filepath + "\*"):

df = pd.read_csv(file)
df['Expiry']= pd.to_datetime(df['Expiry'])
df.to_csv(file,index=False)
