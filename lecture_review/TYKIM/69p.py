i = 1
n = 8
while i < 7:
    print("*" * i)
    i += 1


while n > 0:
    n -= 1
    print("*" * n)

x = 0
y = -1
z = 0

while z < 7:
    x += 1
    y += 1
    z += 1
    print(" " * (7 - x) + "*" * y + "*" * z)

while z > 0:
    x -= 1
    y -= 1
    z -= 1
    print(" " * (7 - x) + "*" * y + "*" * z)
