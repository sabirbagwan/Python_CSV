import os 
import glob
import pandas as pd
os.chdir("E:\\1. Sep18")
extension ='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("combined_csv1.csv", index=False, encoding='utf-8-sig')
