def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
sum=0
n=int(input("Enter n: "))
x=int(input("Enter x: "))
for i in range(0,n+1):
    sum=sum+(x**i)/fact(i)
print(sum)    