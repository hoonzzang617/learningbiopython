n_th = input("n_th pivo: ")

i = 2

pivo_list = [0, 1]
nextone = 0


def pivo(n_th):
    global i
    while i < n_th:
        nextone = 0
        # global nextone
        nextone += pivo_list[i - 2] + pivo_list[i - 1]
        pivo_list.append(nextone)
        i += 1
    return pivo_list[-1]


result = pivo(int(n_th))
print(result)
print(pivo_list)
