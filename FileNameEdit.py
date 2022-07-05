from os import rename, listdir

badprefix = "GFDLNFO_"
fnames = listdir( r'E:\1. SEP18')

for fname in fnames:
    if fname.startswith(badprefix):
        rename(fname, fname.replace(badprefix, '', 1))

        