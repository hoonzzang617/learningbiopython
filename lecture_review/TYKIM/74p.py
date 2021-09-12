seq = input("sequence : ")

revseq = seq[::-1]

bprule = {"A": "T", "T": "A", "G": "C", "C": "G"}
revcompseq = ""
for bp in revseq:
    revcompseq += bprule[bp]

print("reverse sequence is :", revseq)
print("reversde complementary sequence is :", revcompseq)

# print(revseq)
if seq == revcompseq:
    print(f"{seq} is palindromic")
else:
    print(f"{seq} is not palindromic")
