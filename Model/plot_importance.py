import pandas as pd
import matplotlib.pyplot as plt

# Load results
importance = pd.read_csv('top_genes.csv')

# Plot top 20
top20 = importance.head(20)

plt.figure(figsize=(10, 8))
plt.barh(top20['gene'], top20['importance'])
plt.gca().invert_yaxis()
plt.xlabel('Importance Score')
plt.ylabel('Gene')
plt.title('Top 20 Genes Predicting Survival')
plt.tight_layout()
plt.savefig('top_genes.png')
plt.close()

print("Saved: top_genes.png")
