d = {"Daniel":"blue", "SomeoneOne":"blue", "SomeoneTwo":"red"}

def reverse_lookup(value):
	found_keys = []
	for key in d:
		if d[key] == value:
			found_keys.append(key)
	return found_keys


def main():
	print(reverse_lookup("blue")) #['Daniel', 'SomeoneOne']
	print(reverse_lookup("red")) #['SomeoneTwo']

if __name__ == "__main__":
	main()