# =-= coding:utf-8 =-=
import os
import json

events = {}
path = "events"
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        if ".json"in file_path or ".md" in file_path:
            continue
        f = open(file_path,"r",encoding="utf-8")
        res = f.readlines()
        f.close()
        events[int(res[0][:-1])]=[int(res[0][:-1]),file_path,res[1][:-1],res[2][:-1],bool(res[3][:-1]),res[4][:-1]]
f = open("events/index.json","w",encoding="utf-8")
datar = json.dumps(events, sort_keys=True, indent=4, separators=(',', ': '))
f.write(datar)
f.close()