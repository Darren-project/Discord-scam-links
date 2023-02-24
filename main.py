import json
import requests
d1 = requests.get("https://raw.githubusercontent.com/BuildBot42/discord-scam-links/main/list.txt").text
d2 = requests.get("https://raw.githubusercontent.com/DevSpen/scam-links/master/src/links.txt").text
d3 = requests.get("https://raw.githubusercontent.com/Dogino/Discord-Phishing-URLs/main/scam-urls.txt").text
d4 = requests.get("https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/domain-list.json").json()["domains"]
d5raw = requests.get("https://raw.githubusercontent.com/Bananonz/discord-scam-links/main/links.json").text
d5 = d5raw.strip('][').replace('["','').replace('"]','').replace('"','').replace(']','').split('","')
import os
helper = []
f = open("nitroscamlinks.txt", "r")
for f1 in f:
 for line in f1.split():
    helper.append(line)
    print("Adding " + line + " to helper list")
for line in d1.split():
    helper.append(line)
    print("Adding " + line + " to helper list")
for line in d2.split():
    helper.append(line)
    print("Adding " + line + " to helper list")
for line in d3.split():
    helper.append(line)
    print("Adding " + line + " to helper list")
for line in d4:
    helper.append(line)
    print("Adding " + line + " to helper list")
for line in d5:
    helper.append(line)
    print("Adding " + line + " to helper list")
helper = set(helper)
helper2 = []
for i in helper:
    helper2.append(i.replace('https://','').replace('http://',''))
    print("Removing either https:// or http:// and adding " + i + " to helper2 list")
helper = helper2
dd = []
[dd.append(x) for x in helper if x not in dd] 
helper = dd
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
  
