import math
for i in range (int(input())):
    N=int(input())
    l=list(map(int, input().strip().split(" ")))
    min=0
    for j in range (N):
        for k in range (j+1, N):
            if min==0 or math.lcm(l[j], l[k])<min:
                min=math.lcm(l[j], l[k])
    print(min)
