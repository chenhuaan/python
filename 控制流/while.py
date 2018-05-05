number = 50
running = True

while running:
    guess = int(input('Enter an integer: '))
    if guess == number:
        print('Congratulations, you guessed it')
        running =False
    elif guess < number:
        print ('No, it is a smaller num than that number')
    else:
        print ('No, it is a bigger num than that number')
else:
    print ('The while loop is over')
print('Done')