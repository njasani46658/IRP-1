def preventValues(Nikhil):
	"This is going to change argument"
	Nikhil = ['5','6','7','8']
	return (Nikhil)

values = ['1','2','3','4']
print ("Before call : ", values)
values = preventValues(values)
print ("After call : ", values)