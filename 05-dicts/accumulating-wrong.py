
l = [("x",5), ("y",15),("z",10),("y",5)]
d = {}
for k,v in l:
    d.setdefault(k,[]).append(v)

