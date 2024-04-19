# Updates

## Optimizing the SVM ensemble

* **200 models + bootstrap + SGD, no penalty**:
  * _corr threshold = 0.6_
    * E: 108010, V: 6551 when 200 models are used
    * 5396 interactions have nan p-values - removed
    * Number of rejected H0: 276 out of 102614
    * final number of nodes: 6411, final number of edges: 102338


* **500 models + bootstrap + SGD, no penalty**:
  * _corr threshold = 0.6_
    * E: 107962, V: 6595 when 500 models are used
    * 5315 interactions have nan p-values - removed
    * Number of rejected H0: 270 out of 102647
    * final number of nodes: 6438, final number of edges: 102377


| Name                               | |V|  | |E|   | Density   | k        | k weighted | |components| | cc         | s_path     | d  | |communities| | Q        | r squared |
|------------------------------------|------|-------|-----------|------------|--------------|----------|----------|----|---------------|---------|-----------|
| m=500, cor=0.6, ANOVA, unweighted | 6438 | 102377| 0.004941  | 31.803976  | 31.803976    | 192      | 0.786573 | 10.528983| 34 | 250           | 0.937747| 0.57974   |
|



* **700 models + bootstrap + SGD, no penalty**:
    * E: 108720, V: 6587 when 700 models are used
    * ANOVA: 5312 interactions have nan p-values - removed
    * Number of rejected H0: 271 out of 103408
    * final number of nodes: 6428, final number of edges: 103137


## Interactions

### ANOVA

- _error while computing some of the ANOVA tables:_
```python
ValueWarning: covariance of constraints does not have full rank. The number of constraints is 1, but rank is 0
```

The covariance matrix's rank is not full - there exist dependence between model's parameters.
Have ignored all those, suppose there is no interaction between these 2 features.