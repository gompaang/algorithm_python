# 피보나치 수열 - recursive
def fibo(x):
  if x==1 or x==2:
    return x
  else:
    return fibo(x-1) + fibo(x-2)


# 피보나치 수열 - recursive + memoization => top-down
d = [0]*100
def fibo_me(x):
  if x == 1 or x == 2:
    return x

  if d[x] != 0:
    return d[x]
  else:
    d[x] = fibo_me(x - 1) + fibo_me(x - 2)
    return d[x]


# 피보나치 수열 - for 문 => bottom-up
def fibo_for(x):
  d = [0] * x
  d[1] = 1
  d[2] = 1

  for i in range(3, x + 1):
    d[i] = d[i - 1] + d[i - 2]

  return d[x]
