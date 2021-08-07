from Bio import SeqIO

record = SeqIO.read("hemoglobin_subunit_beta.fasta", "fasta")
print(record.id)

