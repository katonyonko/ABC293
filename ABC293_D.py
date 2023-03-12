import io
import sys

_INPUT = """\
6
5 3
3 R 5 B
5 R 3 B
4 R 2 B
7 0
7 6
5 R 3 R
7 R 4 R
4 B 1 R
2 R 3 B
2 B 5 B
1 B 7 B
5 5
5 B 3 R
3 B 4 R
4 B 1 B
5 R 2 R
1 R 2 B
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  G=[[] for _ in range(2*N)]
  ans=[0]*2
  used=[False]*(2*N)
  for i in range(M):
    A,B,C,D=input().split()
    A=int(A)-1
    B=0 if B=='R' else 1
    C=int(C)-1
    D=0 if D=='R' else 1
    if A==C:
      used[2*A]=1
      used[2*A+1]=1
      ans[0]+=1
    else:
      G[2*A+B].append(2*C+D)
      G[2*C+D].append(2*A+B)
  for i in range(N):
    G[2*i].append(2*i+1)
    G[2*i+1].append(2*i)

  def dfs(G,r=0):
    st=[r]
    group=[r]
    while st:
      x=st.pop()
      if used[x]==True:
        continue
      used[x]=True
      for v in G[x]:
        if v==parent[x]:
          continue
        parent[v]=x
        st.append(v)
        group.append(v)
    return group

  parent=[-1]*len(G)
  for i in range(2*N):
    if used[i]==True: continue
    group=dfs(G,i)
    tmp=0
    for g in group:
      if len(G[g])==1: tmp=1
    if tmp==0: ans[0]+=1
    else: ans[1]+=1
  print(*ans)