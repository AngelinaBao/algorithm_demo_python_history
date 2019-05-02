def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'

f = fib(6)
while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print('generator returns value:', e.value)   #捕获错误
        break