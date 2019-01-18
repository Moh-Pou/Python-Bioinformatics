"This is a module containing functions related to bioinformatics."

def fix_protein(protein):
        #Delete all invalid amino acid characters from a protein sequence (a string in between quotation marks) and return the corrected sequence (a string).
        protein=protein.rstrip()        #remove \n 
        protein=protein.upper()         #make the string uppercase
        protein=protein.replace(" ","") #remove spaces in between the characters 
        corrected_aminoacid=''
        for i in range(len(protein)):
            if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
                continue
            corrected_aminoacid=corrected_aminoacid+protein[i]
        return(corrected_aminoacid)

def one_lett_to_three_lett(one_letter):
        #Convert a one-letter amino acid sequence to a three-letter amino acid sequence.
        one_letter=fix_protein(one_letter)     #Fix possible errors in the sequence
        list_one_letter=list(one_letter)
        aa={'R':'ARG','H':'HSD','K':'LYS','D':'ASP','E':'GLU','S':'SER',
        'T':'THR','N':'ASN','Q':'GLN','C':'CYS','U':'SEC','G':'GLY',
        'P':'PRO','A':'ALA','V':'VAL','I':'ILE','L':'LEU','M':'MET',
        'F':'PHE','Y':'TYR','W':'TRP'}
        three_letter=[aa[i] for i in list_one_letter] #a list
        three_letter=' '.join(three_letter)   #a string of amino acids separated by space
        return(three_letter)

def has_stop_codon(dna,frame):
	#Check if a DNA secuence has any stop codon (tga,tag,taa). The output is a True or False.
	stop_codon_found=False
	stop_codons=['tga','tag','taa']
	for i in range(frame,len(dna),3):
		codon=dna[i:i+3].lower()
		if codon in stop_codons:
			stop_codon_found=True
			break
	return stop_codon_found

def reverse(string):
	#Reverse a string.
	return string[::-1]

def complement(dna):
	#Find the complement of a DNA sequence. The input and output are strings.
	basecomplement={'A':'T','C':'G','N':'N','T':'A','G':'C','a':'t','c':'g','n':'n','t':'a','g':'c'}
	letters=list(dna)
	letters=[basecomplement[base] for base in letters]
	return ''.join(letters)
	
def reverse_complement(dna):
	#Find the reverse complement of a DNA sequence. The input and output are strings.
	return complement(reverse(dna))

def read_fasta(myfile):
	#Read a FASTA file and return a dictionary containing all sequences. The input file should be in between quotations.
	try:
        	f = open(myfile)
	except IOError:
	        print("File does not exist!")
	seqs={}
	for line in f:
	        line=line.rstrip()
	        if line.strip():  #pass empty lines    
	                if line[0]=='>': #distinguish header from sequence
	                        words=line.split()
	                        name=words[0][1:]
	                        seqs[name]=''
	                else: #sequence, not hea:qder
	                        seqs[name]=seqs[name]+line
	f.close()
	return seqs
