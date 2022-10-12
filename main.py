import random

file_1 = open("possibilities","r")
file = open("words","r")
wordles = []
possibilites = []
guessed = False
over = False
letters = [] # letters already guessed

for lipe in file_1:
    possibilites += lipe.split()

for line in file:
    wordles += line.split()

ans = random.choice(possibilites)
abc = "abcdefghijklmnopqrstuvwxyz"
listed = list(abc) # The alphabet in a list
over_count = 6

def proximity(var_1, var_2, var_3, A, a, b, c, d):
    # var_1: the guess from the user as a list
    # var_2: the actual answer, as a list
    # var_3: the hint given to the user (made of X, F and T)

    # Trying to see where ONE letter of the guess is situated in the actual answer
    mode = True
    if var_1[A] == var_2[A]:
        # If they're the same letters at the same index
        var_2[A] = "0"
        # Changes the letter of the answer at index A to "0"
        # In case there are more than 1 of the same letter
        var_3[A] = "T"
        for value in letters:
            # If the letter was already guessed before
            if value == var_1[A]:
                mode = False
                # do not add to the list of letters already guessed
    elif var_1[A] == var_2[a] and var_1[A] != var_1[a]:
        # If they're the same letters but at different index
        # AND within the guess, what is at index A is different at index a
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[b] and var_1[A] != var_1[b]:
        # If they're the same letters but at different index
        # AND within the guess, what is at index A is different at index b
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[c] and var_1[A] != var_1[c]:
        # If they're the same letters but at different index
        # AND within the guess, what is at index A is different at index c
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[d] and var_1[A] != var_1[d]:
        # If they're the same letters but at different index
        # AND within the guess, what is at index A is different at index d
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    else:
        mode = False
    if mode:
        # If the letter hasn't been guessed before, add it to the list of letters already guessed
        letters.append(var_1[A])

while not guessed and not over:
    valid = False
    # valid_1 = False (does not seem necessary)
    guess = input("_____:\n").lower()
    x = "XXXXX" 
    hint = list(x) # Puts the hint as a list
    attempt = list(guess) # Puts the guess as a list
    work = list(ans) # Puts the answer as a list
    for word in wordles: 
        if word == guess: # If the guess is in the list of possible words
            valid = True # It is valid
    """
     if len(guess) != 5:
            valid = False
    """
    if valid:
        if guess == ans: # If the guess is the answer
            guessed = True 
            break # We're done
        else:
            proximity(attempt, work, hint, 0, 1, 2, 3, 4)
            # Checks the first letter of the guess to every letter of the actual answer
            proximity(attempt, work, hint, 1, 0, 2, 3, 4)
            # Checks the second letter
            proximity(attempt, work, hint, 2, 0, 1, 3, 4)
            # Checks the third letter
            proximity(attempt, work, hint, 3, 0, 1, 2, 4)
            # Checks the fourth letter
            proximity(attempt, work, hint, 4, 0, 1, 2, 3)
            # Checks the fifth letter
            print("".join(hint)) # Prints the hint
            over_count -= 1 # One less attempt
            for alph in listed: 
                for one in attempt: 
                    if alph == one:
                        # Removing letters that were in the guess from the alphabet list
                        listed.remove(alph)
    else:
        print("Invalid guess!") 
    if over_count == 0:
        over = True
    print("Unused letters:", listed, "\nLetters found:", letters, "\nAttempts left=", over_count)

if guessed:
    print("You win!")
else:
    print("You lost! The answer was:", ans)

"""
str = input("type a")
exec("%s = %d" % (str,0))
print(a)

def proximity(var_1, var_2, var_3, A, a, b, c, d):
    if var_1[A] == var_2[A]:
        var_2[A] = "0"
        var_3[A] = "T"
    elif var_1[A] == var_2[a] or var_1[A] == var_2[b] or var_1[A] == var_2[c] or var_1[A] == var_2[d]:
        var_3[A] = "F"

"""
