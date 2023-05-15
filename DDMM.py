t=int(input())
for i in range(t):
    s=input()
    a=int(s[0]+s[1])
    b=int(s[3]+s[4])
    if(1<=a<=31 and 1<=b<=12)and not(1<=b<=31 and 1<=a<=12):
        print("DD/MM/YYYY")
    elif(1<=b<=31 and 1<=a<=12) and not(1<=a<=31 and 1<=b<=12):
        print("MM/DD/YYYY")
    else:
        print("both")
