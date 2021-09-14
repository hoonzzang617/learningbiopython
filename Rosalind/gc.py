# input_str = input("DNA strings : ")
filename = input("filename : ")
fi = open(filename, "r")
fil = fi.read()
fi.close()

# input_str = ">Rosalind_6404\
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\
# TCCCACTAATAATTCTGAGG\
# >Rosalind_5959\
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\
# ATATCCATTTGTCAGCAGACACGC\
# >Rosalind_0808\
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\
# TGGGAACCTGCGGGCAGTAGGTGGAAT"

input_str = fil

l_str = input_str.split(">")
d_dna_with_gc = dict()
# print(l_str)

for i in l_str:
    if i != "":
        d_dna_with_gc[i[:13]] = 0
        dna_str = i[13:]
        c = dna_str.count("C")
        g = dna_str.count("G")
        gc = (c + g) / len(dna_str) * 100
        d_dna_with_gc[i[:13]] = gc

print(d_dna_with_gc)

l_gc = []
for x in d_dna_with_gc:
    l_gc.append(d_dna_with_gc[x])

gc_max = max(l_gc)

for x in d_dna_with_gc:
    if d_dna_with_gc[x] == gc_max:
        print(x)
        print(round(gc_max, 6))

###################################
# for i in l_str:
#     if i.startswith(">"):
#         d_dna_with_gc[i[1:-1]]=0
#     else:
#         c = i.count('C')
#         g = i.count('G')
#         gc = (c+g)/len(i)*100

