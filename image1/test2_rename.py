import os
import glob

files = glob.glob('./*')

for f in files:
    os.rename(f, 'test2_'+os.path.basename(f))