#!/usr/bin/env python3

from sys import argv

fasta_in = argv[1]

codontable = {
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


def read_fasta(fasta):
    with open(fasta, 'r') as fh:
        entries = {}
        for l in fh:
            # print(l.strip())
            l = l.strip()
            if l.startswith(">"):
                header = l[1:]
                temp_str = ""
                entries[header] = temp_str
            else:
                temp_str += l
                entries[header] = temp_str
    return entries

def rev_comp(entries):
    comp_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}

    for k, v in entries.items():
        rev_v = v[::-1]
        print(rev_v)
        rev_comp_seq = ''
        for char in rev_v:
            if char in comp_dict.keys():
                rev_comp_seq += comp_dict[char]
        entries[k+'_two'] = rev_comp_seq
    print(entries)

def translate(entries):
    string1 = entries['proteinalphabet3'].upper()
    n = 0
    aa_seq = ''
    while string1[n: n+3]:
        temp_codon = string1[n: n+3]
        n += 3
        # print(codontable[temp_codon], end='')
        aa_seq += codontable[temp_codon]
    return aa_seq

if __name__ == '__main__':
    seq_dict = read_fasta(fasta_in)
    my_entries = translate(seq_dict)
    print(my_entries)
    rev_comp(seq_dict)
