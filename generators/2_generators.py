def gen_numbers(n):
    for i in range(n+1):
        yield i


for i in gen_numbers(4):
    print(i)
