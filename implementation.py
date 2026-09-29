from english_words import english_words_lower_set
import random

word = random.choice(list(english_words_lower_set))
hidden_word = ["-"] * len(word)

penalty = 0

while penalty < 12:
    print(" ".join(hidden_word), "/", penalty, "penalties")
    guess = input("$> ").lower()

    if len(guess) == 1:
        if guess in word:
            found = 0
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
                    found += 1
            print("found: ", guess)

        else:
            print("no", guess)
            penalty += 1

    else:
        if guess == word:
            print("you win!")
            break
        else:
            print(guess, "incorrect")
            penalty += 5

    if "-" not in hidden_word:
        print("you win!")
        break

    if penalty >= 12:
        print("you lose!")
        print("the correct answer is", word)
