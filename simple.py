import re 
f = open("test", "r")
y = 0
for i in range(1, 409):
    line = f.readline()
    x = re.search(":", line)
    if x:
        y+=1
        print(y, " - ", line, end='')
    else:
        print(line, end='')
