import random
bag = ['green','green','green','green','green','black','red','red','red','white']
start_purse = 1000
current_purse = start_purse
result = 0
rounds = 3
last_marble = 'none'
print(f'you start the game with {start_purse} golden coins')
for draw in range(1,rounds+1):
    bet = int(input(f'purse: {current_purse} last draw: {last_marble} \nRound {draw} - how much want to bet?: '))
    last_marble = random.choice(bag)
    if last_marble== 'green':
        result = bet
    elif last_marble == 'black':
        result = 10*bet
    elif last_marble == 'white':
        result = -5*bet  
    else:
        result = -bet
    current_purse += result
    if current_purse < start_purse/2:
        print('sorry you lost the game')
        break
    print(f'purse: {current_purse}, last result: ({last_marble}): {result} ')
    print('')
print('starting/ ending purse: ', start_purse, '/', current_purse)
print('gain/loss: ', ((current_purse-start_purse)/start_purse*100), '%')