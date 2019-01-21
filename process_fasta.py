import sys
import getopt

def usage():
        #The help section of the program
        print("""processfasta.py reads a FASTA file and builds a dictionary with all the sequences bigger than a given length.
processfasta.py [-h] [-l <length>] <file name>
-h              print this message
-l              filter all sequences with a length smaller than <length> in integer
                (default <length>=0)
filename        the file has to be in FASTA format""")

o, a = getopt.getopt(sys.argv[1:],'l:h')
opts={}
seqlen=0
for k,v in o:
    opts[k]=v
if '-h' in opts.keys():
    usage(); sys.exit()
if len(a) == 0:
    usage(); sys.exit("Input FASTA file is missing.")
if '-l' in opts.keys():
    if int(opts['-l']) < 0:
        sys.exit("Error: Lenght of sequence should be positive.")
    else:
        seqlen=int(opts['-l']) #get the length
else:
    seqlen = 0

f=open(a[0]) #get the file name
seqs={} #initialize the dictionary
for line in f:
    line=line.rstrip() #ignore \n
    if not line.strip():  #pass empty lines
        continue
    if line[0]=='>': #distinguish header from sequence
        words=line.split()
        name=words[0][1:]
        seqs[name]=''
    else: #read the sequence
        seqs[name]=seqs[name]+line		

shortened_seqs = { i : j for i,j in seqs.items() if len(seqs[i]) > seqlen} #shorten the sequence
print(shortened_seqs)
