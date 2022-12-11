import sys
L=open(sys.argv[1]).readlines()
M=[];f=1
for i in range(1,len(L),7):
	M+=[m:=[[*map(int,L[i][18:].split(','))],eval("lambda old:"+L[i+1][19:]),*[int(l.split()[-1]) for l in L[i+2:i+5]],0]];f*=m[2]
def U(M,R,F):
	for _ in range(R):
		for m in M:
			I,o,d,a,b,_=m;m[5]+=len(I)
			while I:i=F(o(I.pop()));M[b if i%d else a][0]+=[i]
	a,b=sorted(m[5] for m in M)[-2:];return a*b
print([U([[m[:],*o] for m,*o in M],20,lambda x:x//3),U(M,10000,lambda x:x%f)])
