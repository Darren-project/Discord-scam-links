import json
import os
helper = []
f = open("nitroscamlinks.txt", "r")
for f1 in f:
 for line in f1.split():
    helper.append(line)
    print("Adding " + line + " to helper list")
helper = set(helper)
helper2 = []
for i in helper:
    helper2.append(i.replace('https://','').replace('http://',''))
    print("Removing either https:// or http:// and adding " + i + " to helper2 list")
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
data = {
         "urls": df
       }
json.dump(data, f, ensure_ascii=False, indent=4)
f.close()
os.system('ls')
  
