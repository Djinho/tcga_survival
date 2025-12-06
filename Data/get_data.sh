#!/bin/bash

# Expression data
wget -O tcga_expression.gz "https://tcga-pancan-atlas-hub.s3.us-east-1.amazonaws.com/download/EB%2B%2BAdjustPANCAN_IlluminaHiSeq_RNASeqV2.geneExp.xena.gz"

# Clinical/survival data (no .gz)
wget -O tcga_clinical.tsv "https://tcga-pancan-atlas-hub.s3.us-east-1.amazonaws.com/download/Survival_SupplementalTable_S1_20171025_xena_sp"

ls -lh
