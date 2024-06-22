v1=int(input("Enter the first number: "))
v2=int(input("Enter the second number: "))

print ("The Prime Numbers in the range are: ") 
for number in range(v1,v2):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)    