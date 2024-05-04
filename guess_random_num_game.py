import random
targeted_num = random.randint(0, 100)

while True:
    userinput = input("Enter a number or quit(q): ")

    if userinput == 'q' or 'Q':
        break
    else:
        userinput = int(userinput)

    if userinput < targeted_num:
        print("Your number is lesser. Enter again!")
    elif userinput > targeted_num:
        print("Your number is greater. Enter again!")
    else:
        print("You guessed it right!")
        break
print('''|/\GAME OVER/\|''')