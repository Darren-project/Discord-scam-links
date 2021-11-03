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
  #print(line)
  f.write(line + '\n')
f.close()
os.system('cat nitroscamlinks.txt')
  
