# Updates

## Optimizing the SVM ensemble

* **500 models + bootstrap + SGD, no penalty**:
    * E: 107962, V: 6595


## Interactions

### ANOVA

- _error while computing some of the ANOVA tables:_
```python
ValueWarning: covariance of constraints does not have full rank. The number of constraints is 1, but rank is 0
```

The covariance matrix's rank is not full - there exist dependence between model's parameters.
Have ignored all those, suppose there is no interaction between these 2 features.