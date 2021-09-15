from Bio import SeqIO

sequences = []
handle = open("test3.txt", "r")
for record in SeqIO.parse(handle, "fasta"):
    sequences.append(str(record.seq))
handle.close()
s1 = sequences[0]
s2 = sequences[1]

transition = 0
transversion = 0
AG = ["A", "G"]
CT = ["C", "T"]
for nt1, nt2 in zip(s1, s2):
    if nt1 != nt2:
        if nt1 in AG and nt2 in AG:
            transition += 1
        elif nt1 in CT and nt2 in CT:
            transition += 1
        else:
            transversion += 1
print("%0.11f" % (transition / transversion))

