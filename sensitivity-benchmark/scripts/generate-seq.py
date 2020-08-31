#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2020-08-30
# version: 	0.01

import sys
import random

AA = [
    'R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U', 'G', 'P', 'A', 'V',
    'I', 'L', 'M', 'F', 'Y', 'W'
]


def random_aa():
    return AA[random.randrange(20)]


def generate_fasta_seq(length):

    fasta = ">seq\nM"
    for i in range(1, length, 1):
        # x = random.randrange(20)
        fasta += random_aa()

    print(fasta)


def generate_seq_homolog(sequence, percent_identity, number):

    with open(sequence) as f:
        seq = f.readlines()[1].rstrip("\n")

    seq_len = len(seq)
    nb_of_snps = int((100 - percent_identity) / 100 * seq_len)

    for i in range(0, number):
        snps = []
        for j in range(0, nb_of_snps):
            x = -1
            while (x in snps) or (x < 0):
                x = random.randrange(seq_len)
            snps.append(x)
        new_seq = list(seq)
        for m in snps:
            new_seq[m] = random_aa()
        print(">seqm-" + "{:04d}".format(i + 1))
        print(''.join(new_seq))


# Main #
if __name__ == "__main__":

    usage = """

    generate-seq.py

		seq length

		mut sequence identity number

"""
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    if sys.argv[1] == "seq":

        length = sys.argv[2]
        generate_fasta_seq(int(length))

    if sys.argv[1] == "mut":

        if len(sys.argv) < 5:
            print(usage)
            sys.exit(1)
        seq = sys.argv[2]
        identity = float(sys.argv[3])
        number = int(sys.argv[4])
        generate_seq_homolog(seq, identity, number)
