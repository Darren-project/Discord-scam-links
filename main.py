import json
import os
helper = []
f = open("nitroscamlinks.txt", "r")
for f1 in f:
 for line in f1.split():
    helper.append(line)
helper = set(helper)
helper2 = []
for i in helper:
    helper2.append(i.replace('https://',''))
helper = helper2
df = helper
f.close()
f = open("nitroscamlinks.txt", "w")
f.write('')
f.close()
f = open("nitroscamlinks.txt", "a")
for line in df:
  f.write(line + '\n')
f.close()
f = open("nitroscamlinks.json", "w")
f.write('')
f.close()
f = open("nitroscamlinks.json", "a")
f.write('{')
f.write('"urls":{')
lines = len(df)
num = 0
for line in df:
  num = num + 1
  if num = lines:
     f.write('"' + line + '"')
  else:
     f.write('"' + line + '"' + ',')
f.write('}')
f.write('}')
f.close()
os.system('ls')
  
