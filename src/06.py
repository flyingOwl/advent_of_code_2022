import sys
L=open(sys.argv[1]).read()
print([next(c for c in range(n,len(L)) if len(set(L[c-n:c]))==n) for n in [4,14]])
