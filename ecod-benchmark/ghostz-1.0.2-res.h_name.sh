#!/bin/bash

build() {
    path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    cd "$path/../software/ghostz-1.0.2"
    docker build . --tag ghostz:1.0.2
}

makedb() {
    docker run -v $(pwd):/data -u 1000:1000 ghostz:1.0.2 ghostz db  -i sequences/h_name.fasta -o sequences/h_name.fasta.ghostz
}

align() {
    docker run --rm -v $(pwd):/data -u 1000:1000 ghostz:1.0.2 ghostz aln -a 12 -b 150000 -i ./sequences/h_name.fasta -d ./sequences/h_name.fasta.ghostz -o ./results/ghostz-1.0.2-res.h_name.tsv
}

bench_split() {
    split=$1
    docker run --rm -v $(pwd):/data -u 1000:1000 ghostz:1.0.2 bash -c "{ time ghostz aln -a 32 -b 150000 -i ./sequences/h_name.split-$split.fasta -d ./sequences/h_name.fasta.ghostz -o ./results/ghostz-1.0.2-res.h_name.split-$split.tsv ; } 2> ./results/ghostz-1.0.2-res.h_name.split-$split.time"
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
