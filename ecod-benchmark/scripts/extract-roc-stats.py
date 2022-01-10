#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2021-09-22
# version: 	0.01

import sys
import operator
import json


def fmt6_header():
    return [
        "query_id",  # 0
        "subject_id",  # 1
        "pct_identity",  # 2
        "aln_length",  # 3
        "n_of_mismatches",  # 4
        "gap_openings",  # 5
        "q_start",  # 6
        "q_end",  # 7
        "s_start",  # 8
        "s_end",  # 9
        "e_value",  # 10
        "bit_score"  # 11
    ]


def read_prot_family(f):
    prot_fam = {}
    fam_prot = {}
    with open(f) as _f:
        for l in _f:
            lA = l.rstrip('\n').split(' ')
            fam_prot[lA[0]] = lA[1:len(lA)]
            for i in range(1, len(lA)):
                prot_fam[lA[i]] = lA[0]

    return (prot_fam, fam_prot)


def compute_stats(f, prot_fam, fam_prot, bs_threshold, kmer_ratio):

    print("BS threshold: %d" % bs_threshold)

    blast_result = {}
    total_proteins = 0

    for cluster_id in fam_prot.keys():
        # print("Cluster : %s  nb_proteins:%d " % (cluster_id,len(fam_prot[cluster_id])))
        total_proteins += len(fam_prot[cluster_id])
        blast_result[cluster_id] = {}

    with open(f) as _f:
        for l in _f:
            if l[0:7] == "QueryId":  # fix for kaamer output
                continue
            lA = l.rstrip().split("\t")
            query_id = lA[0].split("|")[0]
            subject_id = lA[1].split("|")[0]
            if query_id == subject_id:
                continue
            query_cluster_id = prot_fam[query_id]
            if kmer_ratio:
                if float(float(lA[2])) >= bs_threshold:
                    if subject_id not in blast_result[query_cluster_id]:
                        blast_result[query_cluster_id][subject_id] = True
            else:
                if float(float(lA[11])) >= bs_threshold:
                    if subject_id not in blast_result[query_cluster_id]:
                        blast_result[query_cluster_id][subject_id] = True

    roc_result = {}
    for _cluster_id in blast_result.keys():
        roc_result[_cluster_id] = {
            "tp": 0,
            "tn": 0,
            "fp": 0,
            "fn": 0,
        }

        for hit_id in blast_result[_cluster_id]:
            if _cluster_id == prot_fam[hit_id]:
                roc_result[_cluster_id]["tp"] += 1
            else:
                roc_result[_cluster_id]["fp"] += 1

        for cluster_prot in fam_prot[_cluster_id]:
            if cluster_prot not in blast_result[_cluster_id]:
                roc_result[_cluster_id]["fn"] += 1

        tn = total_proteins - roc_result[_cluster_id]["tp"] - roc_result[
            _cluster_id]["fn"] - roc_result[_cluster_id]["fp"]

        roc_result[_cluster_id]["tn"] = tn

    output_json = f.replace(".tsv", ".roc.json")

    with open(output_json, "a") as output:
        output.write(json.dumps(roc_result))

    output_tsv = f.replace(".tsv", ".fp-tp.tsv")
    with open(output_tsv, "a") as output:
        fp_total = sum(item['fp'] for item in roc_result.values())
        tp_total = sum(item['tp'] for item in roc_result.values())
        output.write("%d\t%d\n" % (fp_total, tp_total))

    return roc_result


def usage():
    return """

extract-roc-stats.py <family-file.tsv> <blast-file>

"""


# Main #
if __name__ == "__main__":

    family_file = sys.argv[1]
    blast_file = sys.argv[2]

    prot_fam, fam_prot = read_prot_family(family_file)

    bs_thresholds = []

    if len(sys.argv) > 3:
        for i in range(0, 100 + 1, 1):
            bs_thresholds.append(i)
            blast_result = compute_stats(blast_file, prot_fam, fam_prot, i,
                                         True)
    else:
        for i in range(0, 2000 + 10, 20):
            bs_thresholds.append(i)
            blast_result = compute_stats(blast_file, prot_fam, fam_prot, i,
                                         False)
