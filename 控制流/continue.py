while True:
    s = input('Enter somethings: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
print('Input is of sufficient length')