t=int(input())
i=2
count=0
while i<=t:
    if t%i==0:

        count=count+1
    i=i+1
if count==1:
    print("it is prime no.")
else:
    print("it is not prime no.")



"""a = int(input())
for i in range(2, a):
    if a % i == 0:
        print(False)
        break
else: 
    print(True)"""

     

