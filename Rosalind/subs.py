s = input("DNA strings : ")
t = input("motif strings : ")

x = len(t)
n = 0


###############################

while True:
    n += 1
    if s[n - 1 :].find(t) == -1:
        break
    print(s[n - 1 :].find(t) + n, end=" ")
    n += s[n - 1 :].find(t)
