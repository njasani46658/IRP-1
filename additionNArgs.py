print("This is a demo of addition of N arguments")

def summation(*vartuple):
	"summarise N number of elements"
	answer = 0
	for element in vartuple:
		answer += int(element)
	return (answer)

print ("Answer is " + str(summation(5,3,6,7,7)))