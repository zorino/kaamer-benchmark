#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2021-10-28
# version: 	0.01

import sys
import random

SPLIT = [10, 100, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

def build_query_set(_file):

    prot_nb = []

    fasta_file = open(_file).read().split(">")
    nb_prot = len(fasta_file)

    split = {}
    for s in SPLIT:
        x = random.sample(range(1, nb_prot-1), s)
        split[s] = sorted(x[0:s+1])

    for s, val in split.items():
        print("Doing split %s.." %s)
        output = open(_file.replace(".fasta", ".split-%d.fasta" % s), "w")
        for v in val:
            output.write(">"+fasta_file[v])

    return True


def usage():
    return """

    build-query-set.py h_name.fasta

"""



# Main #
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(usage())
        exit(1)

    build_query_set(sys.argv[1])
