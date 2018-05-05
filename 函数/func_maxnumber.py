def print_max(a, b):
    if a > b:
        print (a, 'is maxnumber')
    elif a == b:
        print (a, 'is equal to', b)
    else:
        print (b, 'is maxnumber')
#直接传递字面值
print_max(3, 4)

x = 8
y = 8
#已参数的形式传递变量
print_max(x, y)