import sys
S=lambda l:map(set,[l[:len(l)//2],l[len(l)//2:-1]])
def P(z):c=ord(z.pop());return c-[38,96][c>90]
s=t=0;m=[]
for a,b in map(S,open(sys.argv[1])):
	s+=P(a&b);m+=[a|b]
	if len(m)>2:t+=P(m[0]&m[1]&m[2]);m=[]
print([s,t])
