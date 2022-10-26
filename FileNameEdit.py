from os import rename, listdir

badprefix = "bad_"
fnames = listdir( r'E:\SEP')

for fname in fnames:
    if fname.startswith(badprefix):
        rename(fname, fname.replace(badprefix, '', 1))
        
        
###########################

import os
for dpath, dnames, fnames in os.walk("D:\\All\\format1\\exp"):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith("badword_"):
            os.rename(f, f.replace("badword_", ''))

        
