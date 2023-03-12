import io
import sys

_INPUT = """\
6
3 4 7
8 10 9
1000000000 1000000000000 998244353
2 3 6
154 10000 155
3 7 360
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def gcd(a, b):
    while b: a, b = b, a % b
    return a
  def lcm(a, b):
    return a // gcd(a, b) * b
  def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
      t = d
      y = pow(a, t, n)
      if y == 1: continue
      while y != n - 1:
        y = y * y % n
        if y == 1 or t == n - 1: return 0
        t <<= 1
    return 1
  def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
  def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret
  def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

  def read_input(flg):
    if flg==0: A,X,M=map(int,input().split())
    else:
      from random import randint
      A,X,M=randint(1,100),randint(1,100),randint(1,100)
    return A,X,M

  def solve(A,X,M):
    if A==1: return X%M
    else:
      #拡張ユークリッド ax+by=gcd(a,b)となるようなx,yを求める。同時にgcdも求める
      #aとbが互いに素な時、xはmod bにおいてのaの逆元
      def ExtGCD(a, b):
          if b:
              g, y, x = ExtGCD(b, a % b)
              y -= (a // b)*x
              return g, x, y
          return a, 1, 0

      #mが素数と限らない場合にmod.mに置けるaの逆元（aとmが互いに素であることが必要十分条件）を求める関数
      def Inv(a,m):
          return ExtGCD(a,m)[1]%m
      
      # 中国剰余定理。以下を満たすxを求める
      # x≡b1 (mod.m1)
      # x≡b2 (mod.m2)
      import math
      def Ch_Rem(b1,b2,m1,m2):
          g,p,q=ExtGCD(m1,m2)
          d=math.gcd(m1,m2)
          lcm=m1*m2//d
          return (b1+m1//d*(b2-b1)*p)%lcm

      prime=primeFactor(M)
      tmp={}
      for key in prime:
        if prime[key]==1:
          if A%key==0: tmp[key]=1
          elif A%key==1: tmp[key]=X%key
          else: tmp[key]=(pow(A,X,key)-1)*pow(A-1,key-2,key)%key
        else:
          mod=key**prime[key]
          roop=[1]
          used=set([1])
          while roop[-1]*A%mod not in used:
            used.add(roop[-1]*A%mod)
            roop.append(roop[-1]*A%mod)
          idx=roop.index(roop[-1]*A%mod)
          ch,roop=roop[:idx],roop[idx:]
          if X<=len(ch): tmp[mod]=sum(ch[:X])%mod
          else: tmp[mod]=(sum(ch)+sum(roop)*((X-len(ch))//len(roop))+sum(roop[:(X-len(ch))%len(roop)]))%mod
      if len(prime)==0: return 0
      elif len(prime)==1:
        for key in tmp:
          return tmp[key]
      else:
        keys=[key for key in tmp]
        ans=Ch_Rem(tmp[keys[0]],tmp[keys[1]],keys[0],keys[1])
        a=keys[0]*keys[1]
        for i in range(2,len(keys)):
          ans=Ch_Rem(ans,tmp[keys[i]],a,keys[i])
          a*=keys[i]
        return ans
      
  def simple_solve(A,X,M):
    return sum([A**i for i in range(X)])%M

  A,X,M=read_input(0)
  print(solve(A,X,M))