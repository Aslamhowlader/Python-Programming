N=int(input())
for i in range(1,N+1):
    s=N-i
    S=2*i-1
    print(" "*s+"*"*S)
for j in range(N,0,-1):
    s = N - j
    S = 2 * j - 1
    print(" " * s + "*" * S)