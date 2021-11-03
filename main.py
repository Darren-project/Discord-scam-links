helper = []
f = open("nitroscamlinks.txt", "r")
for line in f.readline():
   helper.append(line)
df = helper
f.close()
print(df)
