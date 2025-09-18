def count_lines(fname):
    total_count = 0
    f = open(fname) # get file handle
    c = f.read(1)
    current_line = ""
    while len(c) > 0:
        if c == '\n':
            total_count = total_count + 1
            current_line = ""
        else:
            current_line = current_line + c
        c = f.read(1)
    f.close()
    print("Number of lines in the file:" , total_count)

def generate_lines(fname):
    f = open(fname) # get file handle
    c = f.read(1)
    current_line = ""
    while len(c) > 0:
        if c == '\n':
            yield current_line
            current_line = ""
        else:
            current_line = current_line + c
        c = f.read(1)
    f.close()
    print("Number of lines in the file:" , total_count)

# total_count = 0
# for line in generate_lines("file-generator.py"):
#     print(line.strip())
#     total_count = total_count + 1
# print("new total:",total_count)

for i in range(1,12312345123456789876543234567898765432):
    print(i)
