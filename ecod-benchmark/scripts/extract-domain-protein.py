#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2021-09-18
# version: 	0.01

import sys


def read_ecod_domains(f):

    protein_class = {}
    with open(f) as _f:
        for l in _f:
            if l[0] == "#":
                continue
            lA = l.split("\t")
            protein_class[lA[0]] = {
                "h_name": lA[11].replace(" ","_").replace("/","__").replace('"', '').replace("'", ''),
                "t_name": lA[12].replace(" ","_").replace("/","__").replace('"', '').replace("'", ''),
                "f_name": lA[13].replace(" ","_").replace("/","__").replace('"', '').replace("'", '')
            }

    return protein_class

def read_fasta(f, protein_class):
    with open(f) as _f:
        for l in _f:
            if l[0] == ">":
                _header = l.split("|")
                _id = _header[0].replace(">","")
                for j in ["h_name", "t_name", "f_name"]:
                    filename = j+"/"+protein_class[_id][j]+".fasta"
                    f_out = open(filename, "a")
                    f_out.write(l)
                    f_out.write(_f.readline())
                    f_out.close()
# Main #
if __name__ == "__main__":

    usage = """

extract-domain-protein.py <domain-file> <fasta-file>

"""

    protein_class = read_ecod_domains(sys.argv[1])
    read_fasta(sys.argv[2], protein_class)
