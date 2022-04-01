def reverse_lookup(dictionary,v):
	for k in dictionary:
		if tuple(dictionary[k]) == v:
			return k
	raise LookupError("hello")
with open('anagrams.txt',"r") as r:
	txt = list(r) #Change type from <class '_io.TextIOWrapper'> to list
	# We must have create a dictionary with 4 key
	diction = dict()
	lis_w = txt[0].split(" ") #Create list of words of given text
	# Traverse through list of word and take each word to consider that if all the letter of word in dictionary as key, we only append it
	#to the list of value. If all the letters of the word is not dictionary, we will create new key and create new key-value pairs.
	for i in lis_w:
		if tuple(sorted(i)) not in diction:
			diction[tuple(sorted(i))] = [i]
		else:
			diction[tuple(sorted(i))].append(i)
	for i in diction:
		print(i, ":", diction[i])
	#12.10.2.2 Modify the previous program so that it prints the longest list of anagrams first, followed by
	#the second longest, and so on.
	contra_diction = dict()
	for k in diction:
		contra_diction.update({len(diction[k]):diction[k]})
	for m in sorted(contra_diction,reverse =True):
		print(contra_diction[m])
	#12.10.2.3 In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
	#the board, to form an eight-letter word. What collection of 8 letters forms the most possible
	#bingos?
