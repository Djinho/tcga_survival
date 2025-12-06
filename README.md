# TCGA Survival Prediction

Predicts cancer patient survival from gene expression using Random Survival Forest.

## Results
- **C-index:** 0.729 (1000 genes)
- **Data:** 10,952 patients, 33 cancer types
- **Top genes:** 653553, AADAC, ADAMTSL4, AIM1L, ACVR2B

## Pipeline
1. Download TCGA expression + clinical data
2. Merge on patient ID
3. Train Random Survival Forest
4. Extract feature importance

## Data Source
TCGA Pan-Cancer Atlas via UCSC Xena Browser

## Files
- `Data/` - download scripts and raw data
- `EDA/` - exploratory analysis and plots
- `Model/` - training scripts and results
