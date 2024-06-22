passwd=input("Enter the password: ")
	
SpecialSym =['$', '@', '#']
val = True
	
if len(passwd) < 6:
		print('length should be at least 6')
		val = False
		
if len(passwd) > 12:
		print('length should be not be greater than 8')
		val = False
		
if not any(char.isdigit() for char in passwd):
		print('Password should have at least one numeral')
		val = False
		
if not any(char.isupper() for char in passwd):
		print('Password should have at least one uppercase letter')
		val = False
		
if not any(char.islower() for char in passwd):
		print('Password should have at least one lowercase letter')
		val = False
		
if not any(char in SpecialSym for char in passwd):
		print('Password should have at least one of the symbols $@#')
		val = False
if val:
    print(val)
	
if (passwd):
		print("Password is valid")
else:
		print("Invalid Password !!")
