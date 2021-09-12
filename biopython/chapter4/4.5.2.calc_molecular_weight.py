from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight

seq1 = Seq("ATGCAGTAG")
seq2 = seq1.transcribe()

print(molecular_weight(seq1))
print(molecular_weight(seq1, "DNA"))
print(molecular_weight(seq2, "RNA"))
print(molecular_weight(seq1, "protein"))
