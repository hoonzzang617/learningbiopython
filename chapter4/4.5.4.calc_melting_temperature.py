from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

myseq = Seq("AGTCTGGGACGGCGCGGCAATCGCA")
print(mt.Tm_Wallace(myseq))
