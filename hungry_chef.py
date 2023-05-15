t=int(input())
for i in range(t):
    x,y,n,r=map(int,input().split())
    if r<x*n:
        print(-1)
    elif(r>=y*n):
        print(0,n)
    else:
        z=min(n,(r-x*n)//(y-x))
        print(n-z,z)
        
        
        
        
        
        
        
        
        
        
     
        
        
        
        
        
        
        
        
        
