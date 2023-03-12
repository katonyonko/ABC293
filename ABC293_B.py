import io
import sys

_INPUT = """\
6
5
3 1 4 5 4
20
9 7 19 7 10 4 13 9 4 8 10 15 16 3 18 19 12 13 2 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  ans=[False]*N
  for i in range(N):
    if ans[i]==False: ans[A[i]-1]=True
  ans=[i+1 for i in range(N) if ans[i]==False]
  print(len(ans))
  print(*ans)