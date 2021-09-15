filename = input("filename : ")

fi = open(filename, "r")
fil = fi.readlines()
fi.close()

l_seq = []

for i in fil:
    if i.startswith(">"):
        continue
    l_seq.append(i.strip())


mature_rna = ""
n = 0
total_string = "".join(l_seq)
pre_rna = total_string[0 : len(l_seq[0])]
print(l_seq)
print(pre_rna)
# for i in l_seq:
while True:
    n += 1
    if pre_rna.find(l_seq[n]) != -1:
        print("a")
        pre_rna = pre_rna.replace(l_seq[n], "")
    if n + 1 >= len(l_seq):
        break
mature_rna = pre_rna
print(mature_rna)

codon_table = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "Stop",
    "TAG": "Stop",
    "TGT": "C",
    "TGC": "C",
    "TGA": "Stop",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
x = 0
ptn = ""
# for i in mature_rna:
while True:
    if x % 3 == 0:
        if codon_table[mature_rna[x : x + 3]] == "Stop":
            break
        ptn += codon_table[mature_rna[x : x + 3]]
        x += 3
    if x > len(mature_rna):
        break
print(ptn)

