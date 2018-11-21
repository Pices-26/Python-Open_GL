import random
#guessing function
def guess(machine_max,machine_min):
        machine = random.randrange(machine_min,machine_max)
        return(machine)
#defininf all variables and initial guess
counter = 0
print('hello, think of a number between 1 and 10 and I will guess it')
machine = random.randrange(10)
print('my first guess is ' + str(machine))
print('if this is your nr then enter Y')
print('if your nr is lower enter L')
print('if your nr is higher enter H')
usr = ''
machine_min = 0
machine_max = 10
#guessing loop
while usr != 'y':
    usr = input('please enter your input: ')

    if usr == 'Y':
        print('great, I did it')
        break
    if usr == 'H':
        machine_min = machine
        if machine_max == 10:
            machine_max = 10
        else:
            machine_max = machine_max

        machine =guess(machine_max,machine_min)
        print(machine)
        counter +=1
    if usr =='L':
        machine_max = machine
        if machine_min == 0:
            machine_min = 0
        else:
            machine_min = machine_min

        machine =guess(machine_max, machine_min)
        print(machine)
        counter +=1

print('it took ' + str(counter)+ ' guesses to guess the number')