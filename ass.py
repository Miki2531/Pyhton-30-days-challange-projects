def vol(rad):
    result = 4/3*3.14*rad**3
    return result


print(vol(2))


def ran_check(num, low, high):
    if low < num < high:
        return f' {num} is in the range between {low} and {high}'.format()


print(ran_check(5, 2, 7))
print(ran_check(6, 2, 7))


def up_low(string):
    lower_count = 0
    upper_count = 0

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return lower_count, upper_count


input_string = 'Hello Mr: Mikiyas, how are you this fine Friday'

print(up_low(input_string))
