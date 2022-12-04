import sys
def s(g):a,b=map(int,g.split('-'));return set(range(a,b+1))
D=[[*map(s,l.split(','))] for l in open(sys.argv[1])]
print([sum(a>=b or b>a for a,b in D),sum(any(a&b) for a,b in D)])
