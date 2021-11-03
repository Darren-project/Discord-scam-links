helper = []
f = open("nitroscamlinks.txt", "r")
for f1 in f:
 for line in f1.split():
    helper.append(line)
df = helper
f.close()
print(df)
