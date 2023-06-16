from functools import reduce


def vol(rad):
    result = 4/3*3.14*rad**3
    return result


print(vol(2))


def ran_check(num, low, high):
    # if low < num < high:
    if num in range(low, high+1):
        return f' {num} is in the range between {low} and {high}'


print(ran_check(5, 2, 7))
print(ran_check(6, 2, 7))

# count the number of upper and lower case letter in string statements


def up_low(string):
    lower_count = 0
    upper_count = 0

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1

    print(f"original String: {string}")
    print(f"Lowercase count: {lower_count}")
    print(f"Uppercase count: {upper_count}")
    return lower_count, upper_count


input_string = 'Hello Mr: Mikiyas, how are you this fine Friday'

print(up_low(input_string))

# Method 1


def multiply(number):
    result = reduce(lambda x, y: x*y, number)
    return result


print(multiply([1, 2, 3, -4]))


def sum(number):
    total = 1
    for num in number:
        total = total * num
    return total


print(sum([1, 4, 5, 7, -8]))
# return a uinque list from a list


def unique_list(lst):
    seen_number = []
    for num in lst:
        if num not in seen_number:
            seen_number.append(num)
    return seen_number


print(unique_list([1, 1, 2, 2, 2, 3, 4, 5, 4, 6, 7, 8, 1, 2, 3, 5]))


# check the input from the user
# is digit or not and specify the input range

def user_input():
    choice = 'WRONG'
    acceptable_range = range(1, 10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please input the number between (1-10): ")

        if choice.isdigit() == False:
            print("Sorry input number is not a digit!")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry! The input number is out of range.')
                within_range = False

    return int(choice)


print(user_input())
