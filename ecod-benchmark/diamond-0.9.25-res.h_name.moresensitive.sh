#!/bin/bash

build() {
    path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    cd "$path/../software/diamond-0.9.25"
    docker build . --tag diamond:0.9.25
}

makedb() {
    docker run -v $(pwd):/data -u 1000:1000 diamond:0.9.25 diamond makedb --in sequences/h_name.fasta --db sequences/h_name.fasta
}

align() {
    docker run --rm -v $(pwd):/data -u 1000:1000 diamond:0.9.25 diamond blastp -e 0.01 -k 150000 --more-sensitive --db ./sequences/h_name.fasta.dmnd -q ./sequences/h_name.fasta -o ./results/diamond-0.9.25-res.h_name.moresensitive.tsv
}

bench_split() {
    split=$1
    docker run --rm -v $(pwd):/data -u 1000:1000 diamond:0.9.25 bash -c "{ time diamond blastp -e 0.01 -k 150000 --more-sensitive --db ./sequences/h_name.fasta.dmnd -q ./sequences/h_name.split-$split.fasta -o ./results/diamond-0.9.25-res.h_name.moresensitive.split-$split.tsv ; } 2> ./results/diamond-0.9.25-res.h_name.moresensitive.split-$split.time"
}

bench() {
    sudo bash -c 'sync; echo 3 > /proc/sys/vm/drop_caches'
    for i in 10 100 1000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000
    do
        echo "Split"-$i
        bench_split $i
    done
}

if [ $# -eq 0 ]
then
    echo ""
    echo "Commands: "
    echo ""
    echo "  build     -   will build the docker image of the software"
    echo "  makedb    -   will make the database"
    echo "  align     -   will run the all against all alignments of scop database"
    echo "  bench     -   will run the speed benchmark"
    echo ""
fi

$@
