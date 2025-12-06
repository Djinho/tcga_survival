import pandas as pd

# Load just the first few rows to check structure
expr = pd.read_csv('../Data/tcga_expression.gz', sep='\t', compression='gzip', nrows=10)

print("Shape (first 10 genes):", expr.shape)
print("\nFirst 5 columns:", expr.columns[:5].tolist())
print("\nFirst 5 genes (index):", expr.iloc[:, 0].head().tolist())

# Count total genes and samples without loading full file
import gzip
with gzip.open('../Data/tcga_expression.gz', 'rt') as f:
    header = f.readline().strip().split('\t')
    gene_count = sum(1 for _ in f)

print(f"\nTotal: {gene_count} genes × {len(header)} samples")
