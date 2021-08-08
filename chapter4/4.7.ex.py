from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.SeqUtils import MeltingTemp

seq = Seq("aagtGACAGggatTG")
upperseq = seq.upper()
print(upperseq)
ptn = upperseq.translate(to_stop=True)
print(ptn)
rev_comp = upperseq.reverse_complement()
gc_contents = GC(rev_comp)
melting_temp = MeltingTemp.Tm_Wallace(rev_comp)
print(gc_contents)
print(melting_temp)
