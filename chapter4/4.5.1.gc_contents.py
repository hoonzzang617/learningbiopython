from Bio.Seq import Seq
from Bio.SeqUtils import GC

exon_seq = Seq("ATGCAGTAG")
gc_contents = GC(exon_seq)
print(gc_contents)
