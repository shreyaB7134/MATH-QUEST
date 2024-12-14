from random import randint
from time import time, sleep


def random_num_generator():
    i = 1
    num = ''
    length = randint(1, 3)
    while i <= length:
        num += str(randint(0, 9))
        if num[0] == '0':
            num = num[1:]
            continue
        i += 1
    return num

print('''Mental Maths ==> Practice to become a Human Calculator''')
print("Enter\n\t1 for addition\n\t2 for subtraction\n\t3 for multiplication\n\t4 for divison\n\tEnter 'x' to stop\n\tEnter 'm' to change mode")
mode = input("===>")

score = 0
rounds = 1
while True:
    n1=random_num_generator();n2=random_num_generator()
    if mode == "1":
        expr = f"{n1}+{n2}="
        sol = int(n1) + int(n2)
    elif mode == "2":
        expr = f"{n1}-{n2}="
        sol = int(n1) - int(n2)
    elif mode == "3":
        expr = f"{n1}*{n2}="
        sol = int(n1) * int(n2)
    elif mode =='4':
        print("You only have to enter the quotient of the divison")
        while n1<n2:
            n1=random_num_generator();n2=random_num_generator()
        expr = f"{n1}/{n2}="
        sol = int(n1)//int(n2)
    elif mode == "x":
        exit("Exiting program...")

    expr = str(rounds) + ")" + expr
    print("\t"+expr, end='')
    seci=time()
    user_sol = input("")
    secf=time()
    if user_sol == 'x':
        print(f"\t===========\nScore={score}\n===========")
        exit("Exiting program...")
    if user_sol == 'm':
        print("Enter\n\t1 for addition\n\t2 for subtraction\n\t3 for multiplication\n\t4 for divison\n\tEnter 'x' to stop")
        mode = input("===>")
        continue
    
    time_taken=secf-seci
    time_taken=round(time_taken,3)
    sol = str(sol)
    expr += user_sol
    if user_sol == sol:
        score += 1
    

    print("\033[A" + f"\t{expr.ljust(18)}\tAns={sol.ljust(5)}\tScore={score}/{rounds}\ttime={time_taken}")
    if user_sol!=sol:
        print("\n\tOh no, you have made a mistake...\n\tDont give up,keep practicing to improve!!!\n")
        sleep(1)
    if score%5 ==0 and score != 0:
        print("\n\tHurray, your doing great!!!\n\tContinue practicing to become a human calculator\n")

    rounds += 1
