from random import randrange as r
from time import time as t
no_questions =int(input('how many questions user wants'))
max_num = int(input('Highest number used in practice?: '))
score = 0
answ_list = []
start = t()
for q in range(no_questions):
    num1 = r(1,max_num+1)
    num2 = r(1,max_num+1)
    answ = num1*num2
    u_answ = int(input(f'{num1} *{num2} = '))
    answ_list.append(f'{num1} * {num2} = {answ} you: {u_answ}')
    if u_answ == answ:
        score +=1
    end = t()
print(f'Thank you for playing! \nYou got {score} out of {no_questions} {round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds ({round(end-start)/no_questions,1}) seconds/questions)')
for a in answ_list:
    print(a)
