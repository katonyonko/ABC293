import io
import sys

_INPUT = """\
6
3 3
3 2 2
2 1 3
1 5 4
10 10
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 68 69 70
71 72 73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88 89 90
91 92 93 94 95 96 97 98 99 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import combinations
  H,W=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H)]
  ans=0
  for c in combinations(list(range(H+W-2)),W-1):
    passed=set([A[0][0]])
    root=[0]*(H+W-2)
    for i in range(W-1): root[c[i]]=1
    now=(0,0)
    tmp=0
    for i in range(H+W-2):
      if root[i]==0: nxt=(now[0]+1,now[1])
      else: nxt=(now[0],now[1]+1)
      if A[nxt[0]][nxt[1]] in passed: tmp=1
      else: passed.add(A[nxt[0]][nxt[1]])
      now=nxt
    if tmp==0: ans+=1
  print(ans)