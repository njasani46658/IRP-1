print("This counts word with more than N length")

fileName = input("Enter file name")
minLength = input("Enter minimum length to count words")
counter = 0
with open(fileName,"r") as tempFile:
	for line in tempFile:
		for word in line.split():
			if len(word) > int(minLength):
				counter+=1
tempFile.close()
print("Total %d words found having length more than %s" % (counter, minLength))