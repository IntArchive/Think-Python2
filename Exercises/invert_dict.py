# import module_dictionary_d_used_in_exercise

# def invert_dict():
# 	a = module_dictionary_d_used_in_exercise.dict_letters_to_frequency("aabc");
# 	list_value = a.values();

# 	print();
# invert_dict();
# Maybe we can used value() method. Defined that we can use value() method because it return not list type but a dict_values type
# ___________________________________________________________________________________________________
# import module_dictionary_d_used_in_exercise

# def invert_dict():
# 	a = module_dictionary_d_used_in_exercise.dict_letters_to_frequency("aabc");
# 	dict_inverse = dict();
# 	for i in a:
# 		if a[i] not in dict_inverse:
# 			dict_inverse[a[i]] = [i];
# 		else:
# 			dict_inverse[a[i]].append(i);
# 	return dict_inverse

# print(invert_dict());
# ___________________________________________________________________________________________________
# Solved the problem


import module_dictionary_d_used_in_exercise

def invert_dict():
	a = module_dictionary_d_used_in_exercise.dict_letters_to_frequency("aabc");
	dict_inverse = dict();
	for i in a:
		dict_inverse.setdefault(a[i],[]).append(i);
	return dict_inverse

print(invert_dict());

# Solved the problem



