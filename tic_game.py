game_list = [0, 1, 2]


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


def position_choice():
    choice = 'WRONG'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice")

    return int(choice)


def replacement_choice(game_list, position):
    user_replacement = input("Inter the replacemnent value: ")
    game_list[position] = user_replacement

    return game_list


def gameon_choice():
    choice = 'WRONG'

    while choice not in ['Y', 'N']:
        choice = input("Keep playing the game: ")
        if choice not in ['Y', 'N']:
            print("Sorry, I dont understand, please valid choice Y or N")

    if choice == "Y":
        return True
    else:
        return False


game_on = True
while game_on:
    display_game(game_list)
    position = position_choice()
    replace_value = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()
