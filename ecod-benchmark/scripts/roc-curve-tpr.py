#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2021-10-03
# version: 	0.01

import sys
import plotly.graph_objects as go
import plotly.express as px
import json
import re
import pprint
import numpy as np


def usage():
    return """

roc-curve.py *roc.tsv

"""


def extract_val(res_file):

    x = []
    y = []

    i = -1
    # TPR = TP / TP + FN
    # FPR = FP / FP + TN

    data = []

    data = open(res_file).read().replace("}{", "}],[{")
    data = "[[" + data + "]]"
    json_data = json.loads(data)
    for d in json_data:
        tpr_all = []
        fpr_all = []
        for k, v in d[0].items():
            tpr = float(v["tp"]) / (float(v["tp"]) + float(v["fn"]))
            fpr = float(v["fp"]) / (float(v["fp"]) + float(v["tn"]))
            tpr_all.append(tpr)
            fpr_all.append(fpr)
        fpr_average = float(sum(fpr_all)) / len(fpr_all)
        tpr_average = float(sum(tpr_all)) / len(tpr_all)
        x.append(fpr_average)
        y.append(tpr_average)

    y = [y for _, y in sorted(zip(x, y))]
    x = sorted(x)

    print(x)
    print(y)

    all_x = []
    all_y = []

    x_iter = 0
    for i in np.arange(0, 1, 0.001):
        if x_iter > len(x) - 1:
            break
        if x_iter == 0 and i < x[x_iter]:
            continue
        elif i >= x[x_iter]:
            all_x.append(i)
            all_y.append(y[x_iter])
            x_iter += 1
        else:
            all_x.append(i)
            all_y.append(y[x_iter])

    print(all_x)
    print(all_y)

    return all_x, all_y


def roc_curve(files):

    fig = go.Figure()

    for _file in files:
        _x, _y = extract_val(_file)
        fig.add_trace(go.Scatter(x=_x, y=_y, name=_file, mode='lines'))

    fig.update_xaxes(range=[0, 0.02], constrain='domain', type="log", dtick=1)
    fig.update_yaxes(range=[0, 1], showgrid=True)
    fig.show()


# Main #
if __name__ == "__main__":

    results = {"x": [], "y": {}}
    files = sys.argv[1:]
    roc_curve(files)
