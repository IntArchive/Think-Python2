def dict_letters_to_frequency(strin):
	diction = dict();
	for i in strin:
		if i not in diction:
			diction[i] = 1;
		else:
			diction[i] = diction[i] + 1;
	return diction

def main():
	dict_letters_to_frequency("aabc");

if __name__ == "__main__":
	main();