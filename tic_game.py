game_list = [0, 1, 2]


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


display_game(game_list)


def position_choice():
    choice = 'WRONG'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice")

    return int(choice)


print(position_choice())


def replacement_position(game_list, position):
    user_replacement = input("Inter the replacemnent value: ")
    game_list[position] = user_replacement

    return game_list


print(replacement_position(game_list, 1))
