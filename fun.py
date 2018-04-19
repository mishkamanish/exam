#this function deals with defining functions
#it has two functions pass_fail and factorial
def pass_fail(input_marks):
	"""this function defines passand fail based on value of input no"""
	pass_marks=40
	if input_marks>=pass_marks:
		print("congrats you have passed")
	else:
		print("sorry you have failed")
def  factorial(input_number):
	"""this function calculates factorial"""

	fact=1
	counter=1
	while counter<=input_number:
		fact*=counter
		counter+=1
	return fact
print("now lets see the examples of functions")
check=int(input("for factorial enter 1,for pass_fail enter 2"))
if check==1:
	input_number=int(input("enter a positive integer greater than zero"))
	print(f"the factorial of{input_number} is this:",factorial(input_number))
	print(factorial(input_number))
elif check==2:
	input_marks=int(input("enter marks obtained"))
	pass_fail(input_marks)






	
	
