import DNA_Module as dna
from termcolor import cprint

inputfile = input(str("Enter file to translate: "))
checkfile = input(str("Enter file to verify with: "))

DNA = dna.read_seq(inputfile)
CHECK = dna.read_seq(checkfile)

cds1 = input(("Enter starting CDS: "))
cds2 = input(("Enter finishing CDS: "))
cds1 = int(cds1)
cds2 = int(cds2)
cds1 = cds1-1
cds2 = cds2-3
translated = dna.translate(DNA[cds1:cds2])

cprint('______________________________________________________________', 'magenta')

if CHECK == translated:
    cprint('Translation complete and result correct.', 'green')
    
else:
    cprint("Error in data cleaning.", 'red')
    print('TRANSLATED Amino acid code: ', translated)
    cprint("______________________________________________________________", 'magenta')
    print('GIVEN amino acid codes: ', CHECK)

cprint("______________________________________________________________", 'magenta')
print('Length of DNA sequence: ', len(DNA))
print('Legth of sliced DNA sequence:', len(DNA[21:936]))
print('Length of translated DNA sequence: ', len(translated))
print('Length of solution: ', len(CHECK))