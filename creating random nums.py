import random
random_list=[]
even_list=[]
odd_list=[]
prime_list=[]
for num in range(10):
 random_list.append(random.randint(100,900))
print(random_list)
for num in random_list:
 if num%2==0:
    even_list.append(num)
 
 else:
    odd_list.append(num)   

for number in random_list:
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            prime_list.append(number)

print("The Even list is as follows:")
print(even_list)
print("prime numbers ")
print(prime_list)
print("The Odd list is as follows:")
print(odd_list)