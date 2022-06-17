def f(qty, item, cost):
    return f"{qty} {item} cost ${cost}"


def f(my_list=[]):
    my_list.append('###')
    return my_list


print(f(['Pedro', 'Tania']))
print(f(['Pedro', 'Tania', 'Miguel']))


def avg(a):
    total = 0
    for i in a:
        total = total + i
    print(total)
    print(len(a))
    return total / len(a)


print(avg([1, 2, 3]))
print(avg([1, 2, 3, 4, 5]))


def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')


f(1, 2, 3)
print('\n')

theTuple = (1, 2, 3)
f(*theTuple)


def f(*args):
    print(type(args), args)


names = ('Pedro', 'Tania', 'Miguel', 'Richard')
f(*names)
print('\n' * 2)


# Argument Dictionary Packing
# **kwargs --> dict
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'Key - {key}, value - {value}')


f(foo=1, bar=2, baz=3)


# Argument Dictionary Unpacking
def f(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)


def info(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(f'*args = {args}', type(args))
    print(f'**kwargs = {kwargs}', type(kwargs))


info(1, 2, 'Pedro', 'Tania', 'Miguel', Apple='iPhone', Toyota='Corolla', Console='PS5')
