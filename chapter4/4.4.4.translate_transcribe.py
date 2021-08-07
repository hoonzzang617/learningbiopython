from Bio.Seq import Seq

dna = Seq("ATGCAGTAG")
mrna = dna.transcribe()
ptn = dna.translate()
print(mrna)
print(ptn)
