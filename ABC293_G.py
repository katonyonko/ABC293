import io
import sys

_INPUT = """\
6
10 4
2 7 1 8 2 8 1 8 2 8
1 10
1 9
2 10
5 5
20 10
2 2 2 2 1 1 2 2 1 1 1 2 1 2 1 2 2 1 2 1
12 16
17 18
12 18
4 9
13 13
2 5
6 13
2 14
7 14
8 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,Q=map(int,input().split())
  A=list(map(lambda x:int(x)-1,input().split()))
  count=[0]*2*10**5
  now=0
  l,r=0,0
  ans=[0]*Q
  count[A[0]]=1
  B=max(int(N//(Q**.5)),10)
  query=[list(map(lambda x:int(x)-1,input().split())) for _ in range(Q)]
  query=sorted([(query[i][0]//B,query[i][0],query[i][1],i) for i in range(Q)],key=lambda x: (x[0],x[2]))
  for _ in range(Q):
    x,tl,tr,i=query[_]
    if l>tl:
      for j in range(l-1,tl-1,-1):
        t=A[j]
        now+=count[t]*(count[t]-1)//2
        count[t]+=1
      if r>tr:
        for j in range(r,tr,-1):
          t=A[j]
          count[t]-=1
          now-=count[t]*(count[t]-1)//2
      else:
        for j in range(r+1,tr+1):
          t=A[j]
          now+=count[t]*(count[t]-1)//2
          count[t]+=1
    else:
      if r>tr:
        for j in range(r,tr,-1):
          t=A[j]
          count[t]-=1
          now-=count[t]*(count[t]-1)//2
      else:
        for j in range(r+1,tr+1):
          t=A[j]
          now+=count[t]*(count[t]-1)//2
          count[t]+=1
      for j in range(l,tl):
        t=A[j]
        count[t]-=1
        now-=count[t]*(count[t]-1)//2
    l,r=tl,tr
    ans[i]=now
  print(*ans,sep='\n')