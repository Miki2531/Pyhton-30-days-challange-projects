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


# print(word_string('Mikiya mola'))
# print(word_string('Mikiya shemlis'))

# Give two intgers: return True if the sum of two
# intiger is  20 or on of the intiger is 20. if not return false


def makes_twenty(n1, n2):
    if n1+n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(12, 8))
print(makes_twenty(20, 8))
print(makes_twenty(2, 8))

# change the first and third letter in to capitalize
# methid one


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald('macdonald'))

# method two


def old_macdonald(name):
    new_macdonald = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return new_macdonald


print(old_macdonald('macdonald'))


# reverse sentence
def master_yoga(text):
    wordlist = text.split(' ')
    # reverse_text = ''.join(reversed(wordlist))
    # reverse_text = wordlist[::-1]
    new = ' '.join(wordlist[::-1])
    return new


print(master_yoga('I am home'))
print(master_yoga('I am a software enginner'))


def has_33(list):
    for i in range(0, len(list)-1):
        if list[i] == 3 and list[i+1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 2, 3]))


print(has_33([1, 3, 3]))


def spy_game(list):
    code = [0, 0, 7, 'x']
    for i in list:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))


def check_prime(num):
    if num < 2:
        return 0

    primes = [2]
    x = 3

    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)


check_prime(100)
