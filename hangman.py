from random import choice

def play():
    secret_word = list(choice(["orangutan", "bicycle", "triangle", "parachute", "elephant"]).lower())
    redacted = ["-" for c in secret_word]
    guessed_letters = []
    guesses_left = 6

    while(guesses_left):
        print("".join(redacted))
        letter_input = input("Please enter a letter: ").lower()

        #Checks for invalid input or letters already used
        if len(letter_input) != 1 or not letter_input.isalpha():
            print("Invalid input, please enter one letter\n")
            continue
        if letter_input in guessed_letters:
            print("You have already tried that letter\n")
            continue
        #Correct guess
        if letter_input in secret_word:
            guessed_letters.append(letter_input)
            print(f"Nice, {letter_input} is one of the letters!")
            for i in range(len(secret_word)):
                if secret_word[i] == letter_input and redacted[i] == '-':
                    redacted[i] = letter_input
            #Checks if every letter has been guessed (Won)
            if '-' not in redacted:
                secret_word = "".join(secret_word)
                print(f"\nCongratulations, the word was {secret_word}! \nEnter 'Y' to play again")
                again = input()
                if again.lower() == 'y':
                    play()
                else:
                    print("Thank you for playing!")
                    exit()
        else:
            print(f"Sorry, {letter_input} is not one of the letters!")
            guesses_left -= 1
            if(guesses_left): print(f"Guesses left: {guesses_left}")
        print("\n")

    secret_word = "".join(secret_word)
    print(f"\nYou lost! The word was {secret_word} \nEnter 'Y' to play again")
    again = input()
    if again.lower() == 'y':
        play()
    else:
        print("Thank you for playing!")
        exit()


play()