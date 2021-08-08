from Bio import SeqIO

record = SeqIO.read("J01636.1.fasta", "fasta")
print(record)
