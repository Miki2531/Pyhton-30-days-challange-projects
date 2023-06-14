from random import shuffle


mylist = [' ', 'O', ' ']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def guess_player():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick the number: 0, 1 or 2 ')

    return int(guess)


# guess_player()


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")


mixedup_list = shuffle_list(mylist)
guess = guess_player()
check_guess(mixedup_list, guess)

# 1 return lesser of the two even numbers


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


# take two word_strings and return true when both string
# the word beginds withe the same letter.

def word_string(text):
    wordlist = text.lower().split()
    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False


print(word_string('Mikiya mola'))
print(word_string('Mikiya shemlis'))
