n = 0
for i in range(1,10):
    n = n + 1
    for j in range(n,10):
        k = i * j
        print "%d * %d = %d" % (i,j,k)
