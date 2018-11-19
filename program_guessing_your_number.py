#not the most efficient as it does not close down on range
#work in progress
import random
def guess(machine, usr):
    if usr == 'l':
        guess_machine = random.randrange(machine)
        return(guess_machine)
    else:
        guess_machine = random.randrange(machine, 10)
        return(guess_machine)
counter = 0
print('hello, think of a number between 1 and 10 and I will guess it')
guess_machine = random.randrange(10)
print('my first guess is ' + str(guess_machine))
usr = ''
while usr != 'y':
    print('if this is your nr then enter y')
    print('if your nr is lower enter l')
    print('if your nr is higher enter h')

    usr = input('please enter your input')

    if usr == 'y':
        print('great, I did it')
        break
    else:
        new_guess =guess(guess_machine, usr)
        print(new_guess)
    counter +=1

print('it took ' + str(counter)+ ' guesses to guess the number')