## Thresholding

### WGCNA thresholding

```{r}
library(WGCNA)

Rtab_path="data/pangenomes/Campylobacter_coli/roary_pangenome/gene_presence_absence.Rtab"
df <- read.table(Rtab_path, header=T, row.names=1)
df <-t(df)
dim(df)

#removing all cols that are all 1s (no variation <=> st. dev.=0 <=> cor=NaN <=> error :/)
stdevs <- apply(df, 2, sd)
df <- df[,stdevs!=0]

#correlation matrix
cor_matrix <- cor(df)
View(cor_matrix)
dim(cor_matrix)

#soft threshold
powers = c(1:10)
sft = pickSoftThreshold(df, powerVector = powers, verbose = 5)
```

__Output:__

| nrow | ncol | matrices     |
|------|------|--------------|
| 283  | 5207 | dim of df    |
| 283  | 4257 | dim of cor_matrix |

_soft threshold:_

| Power | SFT.R.sq | slope | truncated.R.sq | mean.k. | median.k. | max.k. |
|-------|----------|-------|----------------|---------|-----------|--------|
| 1     | 0.710    | -1.95 | 0.9780         | 230.00  | 208.00    | 665.0  |
| 2     | 0.615    | -1.76 | 0.8220         | 50.70   | 38.80     | 195.0  |
| 3     | 0.811    | -1.20 | 0.7610         | 24.00   | 15.40     | 104.0  |
| 4     | 0.915    | -1.26 | 0.9150         | 16.30   | 8.38      | 96.5   |
| 5     | 0.752    | -1.26 | 0.7440         | 13.10   | 5.65      | 93.1   |
| 6     | 0.228    | -2.58 | 0.0566         | 11.50   | 4.32      | 91.3   |
| 7     | 0.230    | -2.53 | 0.0699         | 10.50   | 3.38      | 90.4   |
| 8     | 0.231    | -2.48 | 0.0822         | 9.86    | 3.02      | 89.9   |
| 9     | 0.231    | -2.43 | 0.0863         | 9.42    | 2.60      | 89.6   |
| 10    | 0.269    | -3.45 | 0.1500         | 9.10    | 2.18      | 89.4   |

