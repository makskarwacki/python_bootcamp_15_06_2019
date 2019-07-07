def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, you are awesome"


def greet_rafal(greeter_function):
    return greeter_function("Rafał")


print(greet_rafal(say_hello))
print(greet_rafal(be_awesome))

print()
print("=" * 40)
print()


def parent():
    print("Printuje z funkcji parent")

    def first_child():
        print("Printuję z first_child")

    def second_child():
        print("Printuję z second_child")

    first_child()
    second_child()


parent()

print()
print("=" * 40)
print()


def parent(num):
    def first_child():
        print("Cześć jestem Ania ")

        def printuj(x):
            print(x)

        return printuj

    def second_child():
        print("Cześć jestem Cyprian")

    if num == 1:
        return first_child
    else:
        return second_child


print(parent(1))
parent(1)()('xxxx')

print()
print("=" * 40)
print()


def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Coś przed wywołaniem funkcji")
        result = func(*args, **kwargs)
        print("Coś po wywołaniu")
        return result

    return wrapper

def say_whee():
    print("Whee!")

print("Przed udekorowaniem")
say_whee()

print("Po udekorowaniu")
say_whee = my_decorator(say_whee)
say_whee()

@my_decorator
def say_i_like_you(name, x):
    return f"I like You {name}"*x

print(say_i_like_you("Ania", 3))


