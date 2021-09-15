filename = input("filename : ")

fi = open(filename, "r")

l_seq = []

for i in fi:
    if i.startswith(">"):
        continue
    l_seq.append(i.strip())
fi.close()
print(l_seq)

dna = l_seq[0]
sub_seq = l_seq[1]
n = 0


for i in dna:
    for x in sub_seq:
        # if i == x:
        print(dna[n:].find(x) + n + 1, end=" ")
        sub_seq = sub_seq.replace(x, "")  # 이게 꼭 필요하네...?
        # print(sub_seq)
        n = dna[n:].find(x) + n + 1
        # print(n)

