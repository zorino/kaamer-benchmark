#!/bin/bash

makedb() {
    docker run --rm -u 1000:1000 -v $(pwd):/data  ncbi-blast:2.9.0 makeblastdb -dbtype prot -in sequences/h_name.fasta -out sequences/h_name.fasta.blast
}

align() {
    docker run --rm -u 1000:1000 -v $(pwd):/data  ncbi-blast:2.9.0 blastp -evalue 0.01 -max_target_seqs 150000 -num_threads 24 -db sequences/h_name.fasta.blast -query sequences/h_name.fasta  -out ./results/ncbi-blast-2.9.0-res.h_name.tsv -outfmt 6
}

bench_split() {
    split=$1
    docker run --rm -v $(pwd):/data -u 1000:1000 ncbi-blast:2.9.0 bash -c "{ time blastp -evalue 0.01 -max_target_seqs 150000 -num_threads 32 -db sequences/h_name.fasta.blast -query sequences/h_name.split-$split.fasta  -out ./results/ncbi-blast-2.9.0-res.h_name.split-$split.tsv -outfmt 6; } 2> ./results/ncbi-blast-2.9.0-res.h_name.split-$split.time"
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
