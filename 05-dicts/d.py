def load_terms(fname, input, output):
    d = {}
    f = open(fname) # get file handle
    try:
      for line in f: # read file content line by line
          line = line.strip()
          if len(line) > 0 and line[0] != '#': # filter out empty lines and comments
              # example line: "lemma , grundform ; lemma , base form ; N"
              fields = line.split(";")
              # example fields: ['lemma , grundform ', ' lemma , base form ', ' N']
              keys = fields[input].strip().split(",")
              # example keys: ['lemma ',' grundform']
              values = fields[output].strip().split(",")
              for k in keys:
                  # example k: 'lemma '
                  for v in values:
                      d.setdefault(k.strip(),[]).append(v.strip())
    finally:
      f.close() # release file handle
    return d

d = load_terms("terms.csv",0,1)
w = input("word?")
while w != '':
    print(d[w])
    w = input("word?")
