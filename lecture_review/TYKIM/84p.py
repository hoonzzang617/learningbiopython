fi = open("84p.txt", "r")
n = 0
# print(fi)
# fil = fi.readlines()
# print(fil)
for i in fi:
    n += 1
    if n % 2 == 0:
        print(i, end="")


fi.close()

