import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sksurv.ensemble import RandomSurvivalForest

# Load data
df = pd.read_pickle('merged_data.pkl')
gene_cols = [c for c in df.columns if c not in ['sample', 'OS', 'OS.time', 'cancer type abbreviation']]
gene_names = gene_cols[:1000]

X = df[gene_names].values
y_time = df['OS.time'].values
y_event = df['OS'].values

# Split and train
X_train, X_test, y_time_train, y_time_test, y_event_train, y_event_test = train_test_split(
    X, y_time, y_event, test_size=0.2, random_state=42
)

y_train = np.array([(bool(e), t) for e, t in zip(y_event_train, y_time_train)],
                   dtype=[('event', bool), ('time', float)])
y_test = np.array([(bool(e), t) for e, t in zip(y_event_test, y_time_test)],
                  dtype=[('event', bool), ('time', float)])

print("Training model...")
model = RandomSurvivalForest(n_estimators=100, max_depth=5, min_samples_leaf=15, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

print("Calculating importance (takes a minute)...")
result = permutation_importance(model, X_test, y_test, n_repeats=5, random_state=42, n_jobs=-1)

importance = pd.DataFrame({
    'gene': gene_names,
    'importance': result.importances_mean
}).sort_values('importance', ascending=False)

importance.head(50).to_csv('top_genes.csv', index=False)
print("\nTop 20 genes predicting survival:")
print(importance.head(20).to_string(index=False))
