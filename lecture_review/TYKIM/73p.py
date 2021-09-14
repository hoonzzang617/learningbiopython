a = input("start number : ")
b = input("end number : ")

x = int(a)
y = int(b)

aye = 0
bee = 0

for i in range(x, y + 1):

    if i % 2 == 1:
        aye += i


print("sum of all odd integer number :", aye)
