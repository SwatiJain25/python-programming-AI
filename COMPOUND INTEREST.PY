p=int(input("Enter the principal amount "))
t=int(input("Enter the time "))
i=int(input("Enter the interest rate "))
a=p*pow((1+(i/100)),t)
ci=a-p
print(ci)