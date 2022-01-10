#!/bin/bash

makedb() {
    docker run --rm -u 1000:1000 -v $(pwd):/data  kaamer:0.6.0 kaamer-db -make -f fasta -i sequences/h_name.fasta -d sequences/h_name.fasta.kaamer-0.6
}

align() {
    docker network create kaamer-bench
    docker run --name ecod-db --network kaamer-bench -d -u 1000:1000 -v $(pwd):/data kaamer:0.6.0 kaamer-db -server -d sequences/h_name.fasta.kaamer-0.6
    docker run --rm --network kaamer-bench -u 1000:1000 -v $(pwd):/data kaamer:0.6.0 wait-for-it.sh -t 600 ecod-db:8321 -- kaamer -mink 1 -minr 0.001 -search -h http://ecod-db:8321 -i sequences/h_name.fasta -t prot -o results/kaamer-0.6-res.h_name.noalign.tsv -m 150000
    docker stop ecod-db
    docker rm ecod-db
    docker network rm kaamer-bench
}

bench_split() {
    split=$1
    docker network create kaamer-bench
    docker run --name ecod-db --network kaamer-bench -d -u 1000:1000 -v $(pwd):/data kaamer:0.6.0 kaamer-db -server -d sequences/h_name.fasta.kaamer-0.6
    docker run --rm --network kaamer-bench -u 1000:1000 -v $(pwd):/data kaamer:0.6.0 wait-for-it.sh -t 600 ecod-db:8321 -- bash -c "{ time kaamer -mink 1 -minr 0.001 -search -h http://ecod-db:8321 -i sequences/h_name.split-$split.fasta -t prot -o ./results/kaamer-0.6-res.h_name.noalign.split-$split.tsv -m 150000; } 2> ./results/kaamer-0.6-res.h_name.noalign.split-$split.time"
    docker stop ecod-db
    docker rm ecod-db
    docker network rm kaamer-bench
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
    echo "  makedb    -   will make the database"
    echo "  align     -   will run the all against all alignments of scop database"
    echo "  bench     -   will run the speed benchmark"
    echo ""
fi

$@
