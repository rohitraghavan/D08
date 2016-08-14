import sys
import random


def bulls_and_cows_feedback():
	""" This function sets a random number with number of digits
	equal to length passed in the args (default:3) and asks the 
	user to keep guessing until the correct number is arrived at. 
	An indication of bulls (guessed number and random number have 
	common digits at the same position) or cows (gussed number and
	random number have common digits at different positions) is
	given to the user. """

	number_len = 3 #Default number length for random number
	# If one argument with a valid number is provided, use that for random number max length
	if len(sys.argv) == 2:
		try:
			number_len = int(sys.argv[1])
		except:
			print("Invalid number length provided as argument. Reverting to default number length of 3.")
	
	# Set max number of guesses allowed
	max_rounds = 2 ** number_len + number_len
	print("Lets play the mimsmind1 game. You have {} guesses.".format(max_rounds))
	
	# Set a random number with number of digits equal to number_len
	max_number = int('9' * number_len)
	random_number = random.randint(0, max_number)
	random_number = 7

	guess_counter = 0
	guess_message = "\nGuess a {}-digit number: ".format(number_len)
	#Loop till max number of guesses
	while guess_counter < max_rounds:
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

		# If guessed number equals random number, print success and number of attempts and exit
		if guessed_number == random_number:
			print("\nCongratulations. You guessed the correct number in {} tries".format(guess_counter))
			break
		
		#Pad zeros to the beginning of the numbers
		random_number_lst = list('0' * (number_len - len(str(random_number))) + str(random_number))
		guessed_number_lst = list('0' * (number_len - len(str(guessed_number))) + str(guessed_number))
		
		# For bulls: Loop to compare individual digits of guessed and random numbers
		bulls = 0
		number_position = 0
		while number_position < len(guessed_number_lst):
			# If digits at same position are equal, remove the digit from the guessed and 
			# random numbers list and reduce number position
			if guessed_number_lst[number_position] == random_number_lst[number_position]:
				bulls += 1
				guessed_number_lst.pop(number_position)
				random_number_lst.pop(number_position)
				number_position -= 1
			number_position += 1

		# For cows: Loop to check if individual digits of guessed number are in random number
		cows = 0
		number_position = 0
		while number_position < len(guessed_number_lst):
			if guessed_number_lst[number_position] in random_number_lst:
				cows += 1
			number_position += 1

		guess_message = "\n" + str(bulls) + " bull(s), " + str(cows) + " cow(s). Try again: "
	else:
		print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(max_rounds, '0'*(number_len-len(str(random_number)))+str(random_number)))


		

def main():
	bulls_and_cows_feedback()

if __name__ == "__main__":
	main()