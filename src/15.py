import sys
I=[[int(w[2:-1]) for w in l.split(' ') if "=" in w] for l in open(sys.argv[1])]
B=set();S=set();Y=int(2e6);z=Z=Y*2
for x,y,a,b in I:B|=[B,{(a,b)}][b==Y];S|={(x,y,abs(x-a)+abs(y-b))}
def R(Y):
	L=sorted([x-r,x+r] for x,y,m in S if (r:=m-abs(y-Y))>=0);A,E=L[0];O=Z
	for a,e in L:
		if (O:=min(O,E-a+1))>0:E=max(E,e)
	return A,E,O
p,q,_=R(Y);i=0
while z>=Z:a,z,o=R(i);i+=o
print([1+q-p-len(B),Z*(z+1)+i-o])
