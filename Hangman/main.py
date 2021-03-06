import re

#get answer
answer_characters = "What's up, doc?"

answer_characters = answer_characters.upper()

#store known or unkown letters
answer_guesses = []

#determine which characters are known before starting the game
for current_answer_character in answer_characters:
	if re.search("^[A-Z]$", current_answer_character):
		answer_guesses.append(False)
	else:
		answer_guesses.append(True)

#logic of playing the game
guessed_letters = []
num_of_incorrect_guesses = 0

while num_of_incorrect_guesses < 5 and False in answer_guesses:
	print("----------------------")
	print("Guessed Letters: ", end = "")

	for current_guessed_letter in guessed_letters:
		print(f"{current_guessed_letter} ", end = "")
		
	print()

	print(f"Number of incorrect guesses remaining: {5 - num_of_incorrect_guesses}")

	print()

	for answer_index in range(len(answer_characters)):
		if answer_guesses[answer_index]:
			print(answer_characters[answer_index], end = "")
		else:
			print("_", end = "")

	print()
	print()

	letter = input("Enter a letter: ")

	letter = letter.upper()

	if letter not in guessed_letters and len(letter) == 1 and  re.search("^[A-Z]$", letter):
		current_guessed_letter_insert_index = 0

		for current_guessed_letter in guessed_letters:
			if letter < current_guessed_letter:
				break

			current_guessed_letter_insert_index += 1

		guessed_letters.insert(current_guessed_letter_insert_index, letter)

		if letter in answer_characters:
			#letter is in the puzzle
			for current_answer_index in range(len(answer_characters)):
				if letter == answer_characters[current_answer_index]:
						answer_guesses[current_answer_index] = True
		else:
			num_of_incorrect_guesses += 1

print()

#game is over, display win or lose
if num_of_incorrect_guesses < 5:
	print("Congratulations, you solved the puzzle!")
else:
	print("Sorry, you ran out of guesses.")

print()

print(f"{answer_characters} is the answer to the puzzle")