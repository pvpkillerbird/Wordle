import random

file_1 = open("possibilities","r")
file = open("words","r")
wordles = []
possibilites = []
guessed = False
over = False
letters = []

for lipe in file_1:
    possibilites += lipe.split()

for line in file:
    wordles += line.split()

ans = random.choice(possibilites)
abc = "abcdefghijklmnopqrstuvwxyz"
listed = list(abc)
over_count = 6

def proximity(var_1, var_2, var_3, A, a, b, c, d):
    mode = True
    if var_1[A] == var_2[A]:
        var_2[A] = "0"
        var_3[A] = "T"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[a] and var_1[A] != var_1[a]:
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[b] and var_1[A] != var_1[b]:
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[c] and var_1[A] != var_1[c]:
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    elif var_1[A] == var_2[d] and var_1[A] != var_1[d]:
        var_3[A] = "F"
        for value in letters:
            if value == var_1[A]:
                mode = False
    else:
        mode = False
    if mode:
        letters.append(var_1[A])

while not guessed and not over:
    valid = False
    valid_1 = False
    guess = input("_____:\n").lower()
    x = "XXXXX"
    hint = list(x)
    attempt = list(guess)
    work = list(ans)
    for word in wordles:
        if word == guess:
            valid = True
    """
     if len(guess) != 5:
            valid = False
    """
    if valid:
        if guess == ans:
            guessed = True
            break
        else:
            proximity(attempt, work, hint, 0, 1, 2, 3, 4)
            proximity(attempt, work, hint, 1, 0, 2, 3, 4)
            proximity(attempt, work, hint, 2, 0, 1, 3, 4)
            proximity(attempt, work, hint, 3, 0, 1, 2, 4)
            proximity(attempt, work, hint, 4, 0, 1, 2, 3)
            print("".join(hint))
            over_count -= 1
            for alph in listed:
                for one in attempt:
                    if alph == one:
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