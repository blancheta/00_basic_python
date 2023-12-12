

def decorate(func, option):
    print("Passing by decorate")
    print(option)
    def wrapped(param_1):
        print("Print wrapped")
        return func(param_1)

    print("End of decorator")
    return wrapped


@decorate("decorate")
def say_something(param_1):
    print("Hello")
    print(param_1)


say_something("Param 1")