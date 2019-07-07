def italic(func):

    def wrapper(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'

    return wrapper

def bold(func):

    def wrapper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'

    return wrapper

@bold
@italic
def foo(arg):
    return f'to jest {arg}'



def test_decorated_foo():
    assert foo('napis') == '<b><i>to jest napis</i></b>'
