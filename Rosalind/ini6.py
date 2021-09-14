sentence = input("sentence : ")

l_stc = sentence.split()

d_stc = dict()

for i in l_stc:
    if i not in d_stc:
        d_stc[i] = 1
    else:
        d_stc[i] = d_stc[i] + 1

for x in d_stc:
    print(x, d_stc[x])

