class Person:
    nation = "A nation"

    def greeting(self):
        print("(method)greeting:", "Hi")

    def hi1(self):
        self.greeting()

    def hi2(self):
        greeting()


def greeting():
    print("(function)greeting:", "Hello!")


yune = Person()
yune.greeting()
print()
yune.hi1
yune.hi2
