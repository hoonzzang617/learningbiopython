class Person:
    nation = "A nation"

    def greeting(self):
        print("(method)greeting:", "Hi")


yune = Person()
yune.greeting()

print(isinstance(yune, Person))

print("check1", isinstance("hello", (float, int, str, list, dict, tuple)))
print("check2", isinstance("hello", (float, int, list, dict, tuple)))

