from Bio.Seq import Seq

mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn = mRNA.translate()
print(ptn)
ptn1 = mRNA.translate(to_stop=True)
print(ptn1)

