import re
f = open('Prac12.txt','r')
a = []
for lines in f:
    line =lines.split()
    print line
    for i in line:
        if re.findall('^[a-zA-z]+?$',i):
            a.append(i)
a.sort()
print a