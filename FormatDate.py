import glob, os

for old in glob.glob('*.csv'):
    string = old[4] + old[5] + old[6] + old[7] + '-' + old[2] +old[3] +'-'+ old[0] + old[1] +'.csv'
    new = string 
    # new = old[len('GFDLNFO_'):]
    os.rename(old, new)