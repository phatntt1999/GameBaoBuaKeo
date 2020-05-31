from random import randint

print('You want choose Bao, Bua or Keo?')
player = input()
print('-----------')
print('You choose: ' + player)

computer = randint(0,2)

if computer == 0:
    computer = 'Bao'
elif computer == 1:
    computer = 'Bua'
else:
    computer = 'Keo'

print('Computer chooses: ' + computer)
print('-----------')

if computer == player:
    print('Draw')
else:
    if(player == 'Bao'):
        if(computer == 'Keo'):
            print('Lose!!!')
        else:
            print('Win!')
    elif(player == 'Bua'):
        if(computer == 'Keo'):
            print('Win!')
        else:
            print('Lose!!')
    elif(player == 'Keo'):
        if(computer == 'Bao'):
            print('Win!')
        else:
            print('Lose!!')
    else:
        print('Invalid input!!')

