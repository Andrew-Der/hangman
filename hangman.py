import re
from random import randint

MAX_GUESSES = 10
INPUT_FILE_NAME = "input.txt"

if __name__ == "__main__":

    prompt = """
Let's play a game of Hangman. 
You have 10 guesses. Lezz Go!

Hint: type 'list' in prompt to list all used letters."""
    print(prompt)

    with open(INPUT_FILE_NAME, 'r') as f:
        x = f.read().split("\n")

    keyword = x[randint(0,len(x) - 1)]
    keyword = keyword.lower()
    original_keyword = keyword

    mask_keyword = "" 
    for letter in keyword:
        mask_keyword += " " if letter == " " else "_"

    wrong_guesses = 0
    success = False
    guessed_letters = {} 

    while wrong_guesses < MAX_GUESSES and not success:

        print(f"\nRemaining guesses: {MAX_GUESSES - wrong_guesses}")
        print("Keyword: " + mask_keyword)

        input_letter = input("Guess a letter: ").lower()
        # ask until its one letter and a valid character
        if (input_letter == "list"):
            print(list(guessed_letters.keys()))
            continue

        while len(input_letter) != 1 or not re.search("^[a-z]*$", input_letter):
            input_letter = input("Guess only one character (letter or number): ").lower()

        if guessed_letters.get(input_letter):
            print("Already guessed this letter.")
            continue

        guessed_letters[input_letter] = 1
        new_mask_keyword= ""

        if re.search(input_letter, keyword):
            print("Nice got a letter")
            for idx, letter in enumerate(keyword):
                new_mask_keyword += letter if letter == input_letter else mask_keyword[idx]
                    
            mask_keyword = new_mask_keyword
            keyword = keyword.replace(input_letter, "_")

        else:
            print("Not a letter!")
            wrong_guesses += 1

        if re.search("^[ _]*$", keyword):
            success = True


    if success:
        print("\nWooHoo! Game Won")
    else:
        print("\nBoo, Game Lost")
    print(f"Word was : {original_keyword}")