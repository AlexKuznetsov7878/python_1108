def func():
    for i in range(10):
        yield i

x = func()
for val in x:
    print(val)