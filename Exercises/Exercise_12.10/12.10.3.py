# # r = open("words.txt")
# # for i in range(5):
# # 	print(r.readline().strip())

# def reverse_lookup(dictionary,v):
# 	for k in dictionary:
# 		if tuple(dictionary[k]) == v:
# 			return k
# 	raise LookupError("hello")
# 	return None

# def read_5_lines_of_dictionary(diction):
# 	a = 0
# 	for i in diction:
# 		if type(i) == type(5):
# 			raise LookupError("hello")
# 		if a < 5:
# 			print(i, ":",diction[i])
# 			a += 1
# 		else:
# 			break;
# 	return None

# def sorted_by_the_length_of_value_in_dictionary(dicti):
# 	contra_diction = dict()
# 	for k in dicti:
# 		contra_diction.update({len(dicti[k]):dicti[k]})
# 	for m in sorted(contra_diction,reverse =True):
# 		print(contra_diction[m])

# def main():
# 	r = open('C:/Users/Duy/Desktop/Dinh_Minh_Hai/Python/Exercise_12.10/12.10.3/words.txt',"r")
# 	txt = r.readlines() #All of words in file words.txt of Chapter 9
# 	print(type(txt))

# 	a = 0 #Using while loop as a funny
# 	while a < len(txt):
# 		txt[a] = txt[a].strip()
# 		a = a + 1

# 	diction = dict()
# 	for i in txt:
# 		if tuple(sorted(i)) not in diction:
# 			diction[tuple(sorted(i))] = [i]
# 		else:
# 			diction[tuple(sorted(i))].append(i)

# 	for i in diction:
# 		dict_result = dict()
# 		if len(diction[i]) > 1:
# 			print(i, ";", diction[i])
# 	#The question is "How do we arrange the order of key-values pairs follow the length of the value?"

# if __name__ == "__main__":
# 	main()
"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import anagram_sets


def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.
    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.
    word1, word2: strings
    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    sets = anagram_sets.all_anagrams('words.txt')
    metathesis_pairs(sets)