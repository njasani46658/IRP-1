print("This is file handling demo")

with open("sample.txt","r") as tempFile:
	for line in tempFile.readlines():
		print(line)
tempFile.close()