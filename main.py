from operator import is_
import random

def play():
    user = input("Whatis your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r','p', 's'])

    if user == computer:
       return "You and the computer have both chosen{}. It's a tie.".format(computer)

    if is_win(user, computer):
        return "you have chosen{} and the computer have chosen{}. HURRAY! You Won!".format(user, computer)

    else:
        return "you have chosen{} and the computer have chosen{}. You lost".format(user,computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
        
if __name__ == '_main_':
    print(play())
