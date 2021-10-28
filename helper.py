from pathlib import Path
p = Path('.')
import os
q = list(p.glob('**/worker_*.txt'))
files = []
for i in q:
   files.append(i)
   
with open('nitroscamlinks.txt', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            print(fname)
            for line in infile:
                outfile.write(line)
            infile.close()
            os.remove(fname)