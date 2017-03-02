myGlobalVar = 100

def usingGlobal(value):
	"This is going to use global variable"
	myGlobalVar = 50
	answer = value * myGlobalVar
	print ("After multiplying %d with %d , answer is %d" % (value, myGlobalVar, answer))
	print ("Let me change value of global variable")
	global myGlobalVar
	myGlobalVar = 200
	answer = value * myGlobalVar
	print ("After multiplying %d with %d , answer is %d" % (value, myGlobalVar, answer))
	return

usingGlobal(5)
print ("Value of global variable is %d" % myGlobalVar)