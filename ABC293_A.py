import io
import sys

_INPUT = """\
6
abcdef
aaaa
atcoderbeginnercontest
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=[]
  for i in range(len(S)):
    if i%2==0: ans.append(S[i+1])
    else: ans.append(S[i-1])
  print(''.join(ans))