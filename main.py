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
for line in df:
  f.write('"' + line + '"' + ',')
f.write('}')
f.close()
with open('nitroscamlinks.json', 'r') as handle:
    parsed = json.load(handle)
    parsed = json.dumps(parsed, indent=4, sort_keys=True)
    handle.close()
f = open("nitroscamlinks.json", "w")
f.write('')
f.close()
f = open("nitroscamlinks.json", "a")
f.write(parsed)
f.close()
os.system('ls')
  
