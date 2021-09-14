n = input("n : ")
k = input("k : ")
p = int(k)
l_fib = [1, 1]

for i in range(1, int(n) + 1):
    if i < 3:
        continue
    x = l_fib[i - 2] + (l_fib[i - 3]) * p
    l_fib.append(x)

print(l_fib)
print(l_fib[-1])
