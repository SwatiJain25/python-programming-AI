v1=int(input("Enter the first year: "))
v2=int(input("Enter the second year: "))

print ("The Prime Numbers in the range are: ") 
for number in range(v1,v2):
            if number%4==0:
                print(number)   