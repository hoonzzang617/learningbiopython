from Bio.Seq import Seq

exon_seq = Seq("ATGCAGTAG")
g = exon_seq.count("G")
c = exon_seq.count("C")
gc_contents = (g + c) / len(exon_seq) * 100
print(gc_contents)
