from Bio.Seq import Seq

exon_seq = Seq("ATGCAGTAG")
a = exon_seq.count("A")
print(a)
