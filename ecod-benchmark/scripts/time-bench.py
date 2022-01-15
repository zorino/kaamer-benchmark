#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com
# date:    	2020-08-24
# version: 	0.01

import sys
import glob
import pprint
import pandas as pd
import os

pd.options.plotting.backend = "plotly"

SPLITS = [
    10, 100, 1000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000,
    50000
]


def convert_time(val):

    time = val.replace("s", "").split("m")
    minutes = time[0]
    seconds = time[1]

    milliseconds = float(seconds) * 1000

    milliseconds += (float(minutes) * 60 * 1000)

    return milliseconds / 1000


def main(time_files):
    results = {}

    for _f in sorted(time_files):

        _fname = _f.split(".h_name.")
        _soft = _fname[0]
        _fname = _fname[1].split(".")

        if len(_fname) > 2:
            software = _soft.replace("-res", "") + "." + _fname[0]
            split = int(_fname[1].replace("split-", ""))
        else:
            software = _soft.replace("-res", "")
            split = int(_fname[0].replace("split-", ""))

        software = os.path.basename(software)

        if software not in results:
            results[software] = {}
        with open(_f) as f:
            for l in f:
                if l[0:4] == "real":
                    ms = convert_time(l.split()[1])
                    results[software][split] = ms
    data = pd.DataFrame(results)
    data = data.sort_index()
    data.to_csv("zz-time-bench.tsv", sep="\t")

    print(data.head(100))

    fig = data.plot(title="ECOD Benchmark - protein identification time",
                    template="simple_white",
                    log_y=True,
                    width=1200,
                    height=800)

    fig.update_layout(legend=dict(title="Software"),
                      font_family="Courier",
                      font_size=20)

    fig.update_xaxes(title="Number of queries", showgrid=True)
    fig.update_yaxes(title="Execution time (seconds)",
                     showgrid=True,
                     dtick=1,
                     range=[0, 4])
    fig.write_image("zz-time-bench.svg")
    fig.show()


# Main #
if __name__ == "__main__":

    files = sorted(sys.argv[1:])
    time_files = files
    main(time_files)
