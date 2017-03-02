def changeValues(list):
	"This is going to change argument"
	list.append('5')
	return

values = ['1','2','3','4']
print ("Before call : ", values)
changeValues(values)
print ("After call : ", values)