# f = input("FASTA file :")
filename = input("filename : ")
f = open(filename, "r")
fi = f.read()
fil = fi.split()
f.close()


l_seq = []

for i in fil:
    if i.startswith(">"):
        continue
    l_seq.append(i)

print(l_seq)


# for i in l_seq:
#     for x in i:

