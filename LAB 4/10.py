def translate(string):
 	stringlist = []
 	for char in string:
 		if char == "a" or char == "e" or char == "i" or char == "u" or char == "o" or char == " ":
 			stringlist.append(char)
 		else:
 			stringlist.append(char + "o" + char)
 	print "".join(stringlist)
