import re
f = open('from.txt','r')
# print type(f)
for line in f:
    m = re.findall(r'\b[a-zA-z]+', line)
m = sorted(m)
fn = open('to.txt','w')
for word in m:
    s = word + '\n'
    fn.write(s)
fn.close()
