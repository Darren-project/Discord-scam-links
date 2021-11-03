helper = []
f = open("nitroscamlinks.txt", "r")
df = set(str(f.read()))
f.close()
for i in fd:
  helper.append(i.replace('https://',''))
print(helper)
