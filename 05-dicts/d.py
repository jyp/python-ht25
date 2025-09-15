def load_terms():
    d = {}
    f = open("terms.csv")
    for line in f.read().split("\n"):
        if len(line) > 0 and line[0] != '#':
            fields = line.split(";")
            english = fields[1].strip()
            swedish = fields[0].strip()
            for k in english.split(","):
                for v in swedish.split(","):
                    d.setdefault(k.strip(),[]).append(v.strip())
    f.close()
    return d

d = load_terms()
print(d["slice"])
