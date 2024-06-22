bs=int(input("Enter the basic salary: "))
if bs<=10000:
    gs=bs+(20*bs/100)+(80*bs/100)
elif bs<=20000:
    gs=bs+(25*bs/100)+(90*bs/100)    
elif bs>20000:
    gs=bs+(30*bs/100)+(95*bs/100)    

print(gs)    