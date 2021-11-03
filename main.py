helper = []
f = open("nitroscamlinks.txt", "r")
for line in f.split():
   helper.append(line)
df = helper
f.close()
print(df)
