#3.1.3
# enter ipython in the dir you want to read the file from (ideally)
inputfile = "dna.txt"
f = open(inputfile, "r")
# r stands for reading
#read in dna sequence
seq = f.read()
# NB this INCLUDES /n for endofline but print() wont
print(seq)
# use replace to clean hte data
seq = seq.replace("\n", "")
# probably dont have this but safer to remove it just in case
seq = seq.replace("\r", "")
# from source material
table = {
  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
  'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
  'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

table['CCT']
# returns 'P'

# check seq divisible by 3
if len(seq)%3 == 0:
# loop over seq using slices
seq[0:3]
seq[3:6]
# note end point is tsrating point + 3. nest starting point is prev end point ((SO JUST NEED ENDPOINTS)
# can replicate this with a range and step size
length = len(seq)
endpoints = range(0, length, 3)
list(endpoints)
# so this becomes:

protein = ""
if len(seq)%3 == 0:
  for i in range(0, len(seq), 3):
# extract single codon
    codon = seq[i : i+3]
# look up codon and store result
    amino = table[codon]
    # add to protein
    protein += amino

# finally make this a fn

def translate(seq):
  """Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids . Nucleotides are translated in triplets using the table dictionary; each amino acid 4 is encoded with a string of length 1."""
  table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
  }
  protein = ""
  if len(seq)%3 == 0:
    for i in range(0, len(seq), 3):
  # extract single codon
      codon = seq[i : i+3]
  # look up codon and store result
      amino = table[codon]
      # add to protein
      protein += amino
  return protein

In [27]: translate('ATA')
Out[27]: 'I'

# Add a docstring to abv


### 3.1.5 using with to read file
inputfile = 'dna.txt'
with open(inputfile, 'r') as f:
    seq = f.read()


def read_seq(inputfile):
  with open(inputfile, 'r') as f:
      seq = f.read()
  seq = seq.replace("\n", "")
  seq = seq.replace("\r", "")
  return seq

prt = read_seq("protein.txt")
dna = read_seq("dna.txt")

# Note our seq wasn't devisable by 3. why? if you look at the CDS it says 21..938 which means it starts at 91 and ends at 938 HOWEVER it also states that the seq goes from 1 to 1157 (and this is correct, the len(seq) is 1157 but that is not how Python indexes. Python starts at 0 so actually we want 20..938 - because python also doesn't read the last index. SO:

translate(dna[20:938])

# this seems to work, and is the same as prt except ours has a stop codon which we just remove.
translate(dna[20:935])
#how to test that it is the same as protein.txt?
t = translate(dna[20:935])

t == prt
#returns true

# OR

t = translate(dna[20:938])[:-1]
t == prt
#True

