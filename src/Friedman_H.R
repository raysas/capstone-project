if (!requireNamespave('iml'))  
    install.packages('iml') 
# -- CRAN doc https://cran.r-project.org/web/packages/iml/iml.pdf

library(iml)

X <- read.csv('data/graphs-4/X.csv', header = TRUE)

rownames(X) <- X[,1]
X <- X[,-1]

y <- read.csv('data/graphs-4/y.csv')

X <- X[order(rownames(X)),]
y <- y[order(y$genome_id),]

df <- X
df$res <- y$SIR
df$res <- as.factor(df$res)

model <- glm(res ~ ., data = df, family = binomial(link = "logit"))
ia <- Interaction$new(mod)
