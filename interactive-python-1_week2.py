def is_even(number):
    return number % 2 == 0

def is_cool(name):
    return name == 'Joe' or name == 'John' or name == 'Stephen'

def is_lunchtime(hour, is_am):
    return (is_am == 'am' and hour == 11) or (is_am == 'pm' and hour == 12)

def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def interval_intersect(a, b, c, d):
    return (c >= a and c <= b) or (b >=c and b <= d)

def smaller_root(a, b, c):
    import math
    discriminant = (b ** 2) - 4 * a * c
    if discriminant > 0:
        return -(math.sqrt(discriminant) + b) / (2 * a)
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        print 'Error: No real solutions'
        return None

def pig_latin(word):
    word = word.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowel:
        return word[1:] + 'ay'
    else:
        return word + 'way'

def print_digits():
    number = raw_input('Please enter your number:')
    check_interger = 1
    while check_interger:
        try:
            number = int(number)
            check_interger = 0
        except:
            number = raw_input('Please enter an interget and try again:')
    while number < 0 or number > 100:
        print 'Error: Input is not a two-digit number'
        print 'Please try again'
        number = raw_input('Please Enter Your number:')
    ones = int(number) % 10
    tens = (int(number)-ones) / 10
    print 'The tens digit is', tens, 'and the ones digit is', ones
print_digits()


import random
def rpsls():
    rank_str = {'rock':0, 'spock':1, 'paper':2, 'lizard':3, 'scissors':4}
    rank_num = {0:'rock', 1:'spock', 2:'paper', 3:'lizard', 4:'scissors'}

    player_choice = raw_input('Please enter your choice: ')
    while not player_choice in rank_str:
        print 'Not correct input, please try again!'
        player_choice = raw_input('Please enter your choice: ')

    player_choice_num = rank_str[player_choice]
    computer_choice_num = random.randrange(0, 5)
    computer_choice = rank_num[computer_choice_num]

    print 'Player chooses', player_choice
    print 'Computer chooses', computer_choice

    player_win_num = (player_choice_num - 2) % 5
    player_lose_num = (player_choice_num + 2) % 5
    if (computer_choice_num == player_win_num or
        computer_choice_num == ((player_win_num + 1) % 5)):
        print 'Player wins!\n'

    elif (computer_choice_num == player_lose_num or
            computer_choice_num == ((player_lose_num -1) % 5)):
        print 'Computer wins!\n'

    else:
        print 'Player and computer tie!\n'
