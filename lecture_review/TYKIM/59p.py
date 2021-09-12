sentence = "We tried list and we tried dicts also we tried Zen"

l_stc = sentence.split()

d_stc = dict()

for i in l_stc:
    if i not in d_stc:
        d_stc[i] = 1
    else:
        d_stc[i] = d_stc[i] + 1

print(d_stc)

for i in d_stc:
    print(i, d_stc[i])
