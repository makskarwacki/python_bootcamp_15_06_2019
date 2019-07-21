class Parent:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def hello_world(self):
        print("Hello Rafał!!")


class B:

    def __init__(self, c, d):
        self.c = c
        self.d = d
        # self.name = c

    def hello_world(self):
        print("Hello World!!")


class C(Parent, B):

    def __init__(self, name, value, c, d):

        Parent.__init__(self, name, value)
        B.__init__(self, c, d)

    def hello_world(self):
        return B.hello_world(self)


c = C("Rafał", 100, 1, 2)
c.hello_world()
print(c.name)
