#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2021-10-03
# version: 	0.01

import sys
import plotly.graph_objects as go
import plotly.express as px
import os

def usage():
    return """

roc-curve.py *fp-tp.tsv

"""


def extract_uniq_val(res_file):

    x = []
    y = []

    i = -1
    with open(res_file) as f:
        for l in f:
            lA = l.split()
            _x = int(lA[0])
            _y = int(lA[1])
            if i < 0:
                x.append(_x)
                y.append(_y)
                i += 1
                continue
            if _x == x[i]:
                if y[i] < _y:
                    y[i] = _y
            else:
                x.append(_x)
                y.append(_y)
                i += 1

    y = [y for _, y in sorted(zip(x, y))]
    x = sorted(x)

    all_x = []
    all_y = []

    x_iter = 0
    for i in range(0, x[-1]):
        if x_iter == 0 and i < x[x_iter]:
            continue
        elif i == x[x_iter]:
            all_x.append(i)
            all_y.append(y[x_iter])
            x_iter += 1
        else:
            all_x.append(i)
            all_y.append(y[x_iter])

    return all_x, all_y


def roc_curve(files):

    fig = go.Figure()

    for _file in files:

        _fname = _file.split(".h_name.")
        _soft = _fname[0]
        _fname = _fname[1].split(".")
        if len(_fname) > 2:
            software = os.path.basename(_soft) + "." + _fname[0]
        else:
            software = os.path.basename(_soft)

        _x, _y = extract_uniq_val(_file)

        fig.add_trace(go.Scatter(x=_x, y=_y, name=software, mode='lines'))

    fig.update_xaxes(range=[1.5, 4],
                     constrain='domain',
                     type="log",
                     showgrid=True,
                     dtick=1,
                     title="False positive")

    fig.update_yaxes(range=[120000, 150000],
                     showgrid=True,
                     title="True positive")

    fig.update_layout(title="ROC curve - ECOD benchmark",
                      template="simple_white",
                      width=1200,
                      height=800,
                      legend=dict(title="Software"),
                      font_family="Courier",
                      font_size=20)
    fig.write_image("zz-sensitivity-bench.svg")
    fig.show()


# Main #
if __name__ == "__main__":

    results = {"x": [], "y": {}}
    files = sorted(sys.argv[1:])
    roc_curve(files)
