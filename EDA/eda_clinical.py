import pandas as pd
import matplotlib.pyplot as plt

# Load clinical data
df = pd.read_csv('../Data/tcga_clinical.tsv', sep='\t')

# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing OS.time:", df['OS.time'].isna().sum())

# Summary stats
summary = df[['OS', 'OS.time', 'age_at_initial_pathologic_diagnosis']].describe()
summary.to_csv('summary_stats.csv')
print("\nSummary saved to summary_stats.csv")

# Cancer type counts
cancer_counts = df['cancer type abbreviation'].value_counts()
cancer_counts.to_csv('cancer_counts.csv')

# Plot 1: Cancer type distribution
plt.figure(figsize=(12, 6))
cancer_counts.plot(kind='bar')
plt.title('Samples per Cancer Type')
plt.xlabel('Cancer Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('cancer_types.png')
plt.close()

# Plot 2: Survival time distribution
plt.figure(figsize=(10, 5))
df['OS.time'].dropna().hist(bins=50)
plt.title('Overall Survival Time Distribution')
plt.xlabel('Days')
plt.ylabel('Count')
plt.savefig('survival_distribution.png')
plt.close()

# Plot 3: Deaths vs Alive
plt.figure(figsize=(6, 6))
df['OS'].value_counts().plot(kind='pie', labels=['Alive/Censored', 'Died'], autopct='%1.1f%%')
plt.title('Survival Status')
plt.savefig('survival_status.png')
plt.close()

print("\nPlots saved: cancer_types.png, survival_distribution.png, survival_status.png")



# Plot 4: Death rate by cancer type
death_rate = df.groupby('cancer type abbreviation')['OS'].mean().sort_values(ascending=False)
death_rate.to_csv('death_rate_by_cancer.csv')

plt.figure(figsize=(12, 6))
death_rate.plot(kind='bar')
plt.title('Death Rate by Cancer Type')
plt.ylabel('Proportion Died')
plt.tight_layout()
plt.savefig('death_rate_by_cancer.png')
plt.close()
