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
