transition = {"A": "G", "G": "A", "C": "T", "T": "C"}
transversion1 = {"A": "T", "G": "C", "T": "A", "C": "G"}  # same as rule
transversion2 = {"A": "C", "G": "T", "T": "G", "C": "A"}

filename = input("filename : ")
fi = open(filename, "r")
l_seq = []
for i in fi:
    if i.startswith(">"):
        continue
    l_seq.append(i.strip())
fi.close()
# print(l_seq)

n = 0
seq1 = l_seq[0]
seq2 = l_seq[1]
transi = 0
transver = 0
seq3 = ""
for i in seq1:
    seq3 += transversion1[i]
# print(seq3)


for i in seq1:
    if i == seq2[n]:
        pass
    elif i == transition[seq2[n]]:
        transi += 1
    elif i == transversion1[seq2[n]]:
        transver += 1
    elif i == transversion2[seq2[n]]:
        transver += 1
    n += 1
print(transi)
print(transver)
print(transi / transver)
