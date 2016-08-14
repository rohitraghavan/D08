import sys
import random


def basic_feedback():
	""" This function sets a random number with number of digits
	equal to length	passed in the args (default:1) and asks the
	user to guess a	lower or higher number until the correct number 
	is arrived at. """

	number_len = 1 #Default number length for random number
	# If one argument with a valid number is provided, use that for random number max length
	if len(sys.argv) == 2:
		try:
			number_len = int(sys.argv[1])
		except:
			print("Invalid number length provided as argument. Reverting to default number length of 1.")
	
	print("Lets play the mimsmind0 game.")
	
	# Set a random number with number of digits equal to number_len
	max_number = int('9' * number_len)
	random_number = random.randint(0, max_number)

	guess_counter = 0
	guess_message = "\nGuess a {}-digit number: ".format(number_len)
	while True:
		guess = input(guess_message)
		try:
			guessed_number = int(guess)
		except:
			guess_message = "\nInvaild input. Try again: "
			continue
		#If input number length is less than number_len, alert the user
		if len(guess) != number_len:
			guess_message = "\nInvaild input. Try again: "
			continue
		guess_counter += 1
		
		# Print appropriate message is entered number is less than or greater than random number
		if guessed_number < random_number:
			guess_message = "\nTry again. Guess a higher number: "
		elif guessed_number > random_number:
			guess_message = "\nTry again. Guess a lower number: "
		# If guessed number equals random number, print success and number of attempts and exit
		elif guessed_number == random_number:
			print("\nCongratulations. You guessed the correct number in {} tries".format(guess_counter))
			break

def main():
	basic_feedback()

if __name__ == "__main__":
	main()