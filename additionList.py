print("This is list addition demo")

def summation(list):
	"summarise elements of list"
	answer = 0
	for element in list:
		answer += int(element)
	return (answer)

inputs = input("Please enter list elements in comma separated form")
List=inputs.split(',')
answer = summation(List)
print ("Answer is " + str(answer))