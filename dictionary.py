D= {1:"One", 2:"Two", 3:"Three", 4: "Four", 5:"Five"}
D[6]="Six"
print(D)
del D[2]
print(D)
print("Is Key 6 Present --> ",2 in D)
print(len(D)) 
D= {1:1, 2:2, 3:3, 4:4, 5:5}
sum1=0
for i in D:sum1 = sum1 + D[i] 
print(sum1)