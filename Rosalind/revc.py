dna = input("string : ")

reverse = dna[::-1]

dic = {"A": "T", "T": "A", "G": "C", "C": "G"}

reverse_comp = ""

for i in reverse:
    reverse_comp += dic[i]

print(reverse_comp)

