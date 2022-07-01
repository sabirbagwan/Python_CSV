from numpy import dtype
import pandas as pd
import glob
from datetime import timedelta

filepath = r"C:\Users\sabir\Desktop\nifty5months\New folder"

for file in glob.glob(filepath + "\*.csv"):

    df = pd.read_csv(file)
    print(df(dtype))
    ndf=df[df["Time"] - timedelta(days=0, hours=0, minutes=1)]
    ndf.to_csv(file,index=False)
