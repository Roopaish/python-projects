import random

def play():
    user = input("What's your choice? 'r' for rock , 's' for scissors and 'r' for rock : ")
    computer = random.choice(['r','p','s'])

    #r>s,s>p,p>r
    #function ends at 1st return
    if user == computer:
        return 'tie'
    
    if is_win(user,computer):
        return 'You Won!'

    return 'You Lost!'


def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())