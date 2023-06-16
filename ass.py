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


def multiply(number):
    result = reduce(lambda x, y: x*y, number)
    return result


print(multiply([1, 2, 3, -4]))

# return a uinque list from a list


def unique_list(lst):
    seen_number = []
    for num in lst:
        if num not in seen_number:
            seen_number.append(num)
    return seen_number


print(unique_list([1, 1, 2, 2, 2, 3, 4, 5, 4, 6, 7, 8, 1, 2, 3, 5]))
