x = 50

def func_local(x):
    print ('x is', x)
    x = 20
    print ('x is change to', x)

func_local(x)
print ('x is still', x)