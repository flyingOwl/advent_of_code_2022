import sys
S=lambda x,y,z:{(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}
L={(*map(int,l.split(',')),) for l in open(sys.argv[1])}
A=[n for l in L for n in S(*l)-L]
O=F={(-1,)*3}
while F:O|=F;F={n for f in F for n in S(*f)-L if min(n)>-2 and max(n)<24}-O
print([len(A),sum(a in O for a in A)])
