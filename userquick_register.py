def
def sum(a,b):	
	print(a+b)
def diff(a,b):
	print(a-b)
def mult(a,b):
	print(a*b)
def div(a,b):def calculator():
	print(a/b)

	print("welcome user")
	print("Please select your choice")
def mychoice():
	print("1.find sum")
	print("2.find subtraction")
	print("3.find multiplication")
	print("4.find division")
	print("5.exit program")
def inputdetails():
	choice=int(input("please enter your choice:"))
	choice=mychoice()
	if(choice==1):
		sum(a,b)
	elif(choice==2):
		diff(a,b)
	elif(choice==3):
		mult(a,b)
	elif(choice==4):
		div(a,b)
	else:
		print("invalid")
def inputdet():

	print("print enter two numbers")
	a=int(input("please enter the first number:"))
	b=int(input("please enter the second number:"))
	
calculator()
mychoice()
inputdetails()
inputdet()