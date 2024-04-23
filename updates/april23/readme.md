# Updates 

## Some results:


* Trying on 200 randomized SVM, |corr|<0.4 - Acinetobacter_baumannii + amakicine:
    * E: 224744, V: 6951 when 200 models are used
    * 16770 interactions have nan p-values - removed
    * Number of rejected H0: 1117 out of 207974
    * final number of nodes: 510, final number of edges: 1117

![](image.png)

* E: 398210, V: 5311 when 200 models are used, with corr threshold=0.4; species=Acinetobacter_baumannii, drug=amikacin.

E: 222504, V: 6953 when 200 models are used, with corr threshold=0.4; species=Campylobacter_coli, drug=ciprofloxacin.
    * 16138 interactions have nan p-values - removed
    * Number of rejected H0: 1275 out of 206366
    * final number of nodes: 544, final number of edges: 1275
