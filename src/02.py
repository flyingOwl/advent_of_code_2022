import sys
G=lambda j:[2,0,1,2,0][j:]
d=[(ord(l[0])-65,ord(l[2])-88) for l in open(sys.argv[1]).readlines()]
s=[0,0]
for a,b in d:
	s[0]+=1+b+G(a).index(b)*3
	s[1]+=1+b*3+G(a)[b]
print(s)
