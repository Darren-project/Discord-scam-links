helper = []
f = open("nitroscamlinks.txt", "r")
df = set(str(f.read()))
f.close()
for i in df:
  helper.append(i.replace('https://',''))
print(helper)
