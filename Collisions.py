
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = []
    for __ in range(N):
        A.append(input())
    coll = 0
    for j in range(M):
        count = 0
        for i in range(N):
            count += (A[i][j] == "1")
        coll += (count*(count-1))//2 
    print(coll)
