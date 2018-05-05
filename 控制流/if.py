number = 23
guess = int(input('Enter an inter: '))
if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you don\'t win any prizes!)')
elif guess < number:
    print('No, it is a smaller num than that number')
else:
    print('No, it is a bigger num than that number')
print('Dnoe')