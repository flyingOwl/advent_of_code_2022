import sys
L=open(sys.argv[1]).read()
F=lambda n:next(c for c in range(n,len(L)) if len(set(L[c-n:c]))==n)
print([F(4),F(14)])
