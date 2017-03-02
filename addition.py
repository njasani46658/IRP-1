print("This is addition demo")

def summation(arg1, arg2):
	"summarise two integers"
	return (arg1 + arg2)

number1 = input("Enter first number")
number2 = input("Enter second number")
print ("Passing two integers")
answer = summation(int(number1),int(number2))
print ("Answer is " + str(answer))