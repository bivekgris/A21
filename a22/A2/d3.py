d={"y":120, "w": 1100, "m": 190, "n": 1050, "l": 3200, "j": 400}

for k in d.keys():
    if d[k]>200:
        d[k]=d[k]+600

print(repr(d))
         
    