# Given a DNA sequence, find the positions of donor splice site candidates. Splice sites always start with the letters gt.
dna = input("Enter DNA sequence:")
pos = dna.find('gt',0) #position of the donor splice site
if pos == -1: 
    print("No donor splice site candidate!")
while pos > -1:
    print("Donor splice site at position %d"%pos)
    pos = dna.find('gt',pos+1)
