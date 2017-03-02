print("Let me check your maths")
number1 = input("Enter first number")
number2 = input("Enter second number")
answer = input("What is your answer?")
myAnswer = int(number1) + int(number2)
if int(answer) == myAnswer:
	print ("Your answer is correct")
else:
	print ("You need to study math")