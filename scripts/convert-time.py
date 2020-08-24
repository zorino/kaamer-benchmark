#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2020-08-24
# version: 	0.01

import sys


def convert_time(val):

    milliseconds = 0
    centieme = val.split(".")
    if len(centieme) > 1:
        milliseconds += int(centieme[1]) * 10

    facteur_multiplicatif = 1
    val_split = val.split(".")[0].split(":")
    i = len(val_split) - 1
    while i >= 0:
        milliseconds += int(val_split[i]) * 1000 * facteur_multiplicatif
        facteur_multiplicatif = facteur_multiplicatif * 60
        i = i - 1

    # print(milliseconds)
    return "%d" % milliseconds


# Main #
if __name__ == "__main__":

    table_file = sys.argv[1]
    with open(table_file) as f:
        for l in f:
            vals = l.rstrip("\n").split("\t")
            out = ""
            for v in vals:
                # convert_time(v)
                out += convert_time(v) + "\t"
            print(out)
