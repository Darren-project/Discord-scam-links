f = open("nitroscamlinks.txt", "r")
df = set(str(f.read()).replace('https://',''))
f.close()
print(df)
