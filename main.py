helper = []
f = open("nitroscamlinks.txt", "r")
for line in f.read():
   helper.append(line)
df = set(helper)
f.close()
print(df)
