import pandas as pd
import glob

filepath = r"E:\\ALL"

for file in glob.glob(filepath + "\*"):
    df = pd.read_csv(file)
    colnames = ['Volume', 'Open Interest']
    df = df.drop([x for x in colnames if x in df.columns], axis=1)
    df.to_csv(file,index=False)
