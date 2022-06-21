
import pandas as pd
import glob

filepath = r"E:\Allfiles"

for file in glob.glob(filepath + "\*"):

    df = pd.read_csv(file)
    ndf=df[df.Ticker != "BANKNIFTY*"]
    ndf=df[df["Ticker"].str.contains("NIFTY-I.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTY-II.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTY-III.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTYIT-I.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTYIT-II.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTYMID50-I.NFO") == False]
    ndf=df[df["Ticker"].str.contains("NIFTYMID50-II.NFO") == False]
    ndf=df[df["Ticker1"].str.contains("BANKNIFTY-") == False]

    ndf.to_csv(file,index=False)
    print(file)
