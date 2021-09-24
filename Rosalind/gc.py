filename = input("filename : ")
fi = open(filename, "r")
fasta = ""
n = 0
for i in fi:
    if i.startswith(">"):
        fasta += "\n" + i
    else:
        fasta += i.strip()
    if n == 0:
        fasta = fasta.lstrip()
    n += 1
fi.close()

# print(fasta)

l_fasta = fasta.split("\n")
print(l_fasta)
dict_dna = dict()
x = 0
for i in l_fasta:
    if l_fasta[x].startswith(">"):
        # dict_dna[l_fasta[x]] = ""
        pass
    else:
        dict_dna[l_fasta[x - 1]] = i
    x += 1
print(dict_dna)
l_gc = []
for i in dict_dna:
    dna = dict_dna[i]
    c = dna.count("C")
    g = dna.count("G")
    gc = (c + g) / len(dna) * 100
    l_gc.append(gc)

print(l_gc)
print(round(max(l_gc), 6))


# # input_str = input("DNA strings : ")
# filename = input("filename : ")
# fi = open(filename, "r")
# fil = fi.read()
# fi.close()

# input_str = fil

# l_str = input_str.split(">")
# d_dna_with_gc = dict()
# # print(l_str)
# for i in l_str:
#     if i != "":
#         d_dna_with_gc[i[:13]] = 0
#         dna_str = i[13:]
#         c = dna_str.count("C")
#         g = dna_str.count("G")
#         gc = (c + g) / len(dna_str) * 100
#         d_dna_with_gc[i[:13]] = gc
# print(d_dna_with_gc)
# l_gc = []
# for x in d_dna_with_gc:
#     l_gc.append(d_dna_with_gc[x])

# gc_max = max(l_gc)

# for x in d_dna_with_gc:
#     if d_dna_with_gc[x] == gc_max:
#         print(x)
#         print(round(gc_max, 6))

###################################
# for i in l_str:
#     if i.startswith(">"):
#         d_dna_with_gc[i[1:-1]]=0
#     else:
#         c = i.count('C')
#         g = i.count('G')
#         gc = (c+g)/len(i)*100

