print("This is to show you power of Python List")
List = ['Hi', 'This', 'is', '#', 1, 'feature']
print ("Actual list is like this " + str(List))
List[4] = 2
print ("Updated list is like this " + str(List))
List.append("New")
print ("Updated list is like this " + str(List))
del List[4]
print ("Updated list is like this " + str(List))
List.reverse()
print (List*2)