import io
import sys

_INPUT = """\
6
4
12
2
36
1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def Base_10_to_n(X, n):
    res=[]
    d=1
    while pow(n,d)<=X: d+=1
    for i in range(d):
      res.append(X//pow(n,d-1-i))
      X%=pow(n,d-1-i)
    return res[::-1]

  def solve(T,query):
    res=[]
    for _ in range(T):
      N=query[_]
      if N==2: res.append(1)
      else:
        ans=2
        d=3
        while N>=pow(2,d-1):
          l,r=0,10**9+1
          while r-l>1:
            mid=(l+r)//2
            if pow(mid,d-1)<=N: l=mid
            else: r=mid
          x=Base_10_to_n(N,l)
          if len(x)==d and len([1 for i in range(len(x)) if x[i]>1])==0: ans+=1
          d+=1
        res.append(ans)
    return res

  def simple_solve(T,query):
    res=[]
    for _ in range(T):
      N=query[_]
      ans=0
      for i in range(1,N):
        x=Base_10_to_n(N,i+1)
        if len([1 for i in range(len(x)) if x[i]>1])==0: ans+=1; print(i+1)
      res.append(ans)
    return res

  def read_input(flg):
    if flg==0:
      T=int(input())
      query=[]
      for _ in range(T):
        N=int(input())
        query.append(N)
    else:
      from random import randint
      T=10
      query=[]
      for _ in range(T):
        N=randint(2,1000)
        query.append(N)
    return T,query

  T,query=read_input(0)
  print(*solve(T,query),sep='\n')