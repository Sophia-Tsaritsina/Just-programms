f = open('text.txt', 'w')
s1 = 10
for i in range(1, s1+1):
    f.write(*range(i, i*s1+1, i), sep='\t')
f.close()
