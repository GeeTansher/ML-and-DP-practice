# health management syatem.
def getdate():
	import datetime
	return datetime.datetime.now()
names = { "1" : "Harry" , "2" : "Rohan" , "3" : "Hammad" }
def name():
	n = input("Enter the person's name to edit his/her data:-\nType 1 for Harry, 2 for Rohan, 3 for Hammad::")
#	n = int(input())
	return n
na = name()
a = getdate()


	