import pandas as pd
import numpy as np

print("Loading clinical data...")
clinical = pd.read_csv('../Data/tcga_clinical.tsv', sep='\t')
clinical = clinical[['sample', 'OS', 'OS.time', 'cancer type abbreviation']].dropna()
print(f"Clinical: {clinical.shape[0]} samples")

print("Loading expression data (this takes a minute)...")
expr = pd.read_csv('../Data/tcga_expression.gz', sep='\t', compression='gzip', index_col=0)
expr = expr.T  # samples as rows
expr.index.name = 'sample'
expr = expr.reset_index()
print(f"Expression: {expr.shape[0]} samples × {expr.shape[1]-1} genes")

print("Merging...")
merged = expr.merge(clinical, on='sample', how='inner')
print(f"Merged: {merged.shape[0]} samples")

# Save for modeling
merged.to_pickle('merged_data.pkl')
print("Saved: merged_data.pkl")
