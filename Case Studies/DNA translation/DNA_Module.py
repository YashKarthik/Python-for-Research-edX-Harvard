#Given data: dna.txt, protein.txt

def read_seq(inputfile):   
    """Reads and returns text after removing special characters: '\n' and'\r'"""

    with open(inputfile, 'r') as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    seq = seq.replace('\r', '')

    return seq

def translate(seq):

    """Translates a string containing a nucleotide sequence into a string
    containing a sequence of corresponding amino acid codes. Nucleotides 
    are translated in triplets using table dictionary; each amino acid is
    encode in stri g length 1. 
     """


    # Translation table
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

    # Check if seq is div by 3
        # Loop over seq for 3-letter codons
            # Lookup each 3-letter codon
            #Translate each 3-letter codon into corresponding protein
            # Stor the result
    protein = ''

    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]

    return protein

