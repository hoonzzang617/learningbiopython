from Bio.Seq import Seq

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
strt_idx = tatabox_seq.find("ATG")
end_idx = tatabox_seq.find("TAG", strt_idx)
orf = tatabox_seq[strt_idx : end_idx + 3]
print(orf)

