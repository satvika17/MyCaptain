n=int(input("enter the nth number:"))
i=0
a=0
b=1
while(i<n):
    if(i<=1):
        Next=i
    else:
        Next=a+b
        a=b
        b=Next
    print(Next)
    i+=1
