print("This is exception handling demo")
try:
	#file = open("sample1.txt","r")
	sys.exit()
except ZeroDivisionError:
	print("I cought an IO Error")
except IOError:
	print("I cought an IO Error")
except Exception:
	print("I cought an exception")
print("I prevented system exit")
