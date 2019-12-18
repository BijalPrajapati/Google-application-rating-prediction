#library(randomForest)
require(caTools)
data <- read.csv("C:\\Users\\Bijal\\Documents\\Predicting-Application-Rating-of-Google-Play-Store-master\\final4.csv",header=FALSE)
dim(data)
head(data)
str(data)
data$v7<-as.factor(data$v7)

table(data$V7)

#data prediction

set.seed(123)
ind <- sample(2, nrow(data), replace = TRUE, prob = c(0.7, 0.3))
train <- data[ind==1,]
test <- data[ind==2,]

#------edureka-----------
# implement model
# optimised value of mtry





#------------end-------------




# Random Forest
library(randomForest)
set.seed(222)
rf <- randomForest(NSP ~., data=train)
print(rf)
attributes(rf)

# Prediction & Confusion Matrix - train data
library(caret)
p1 <- predict(rf, train)
confusionMatrix(p1, train$NSP)

# PRediction & Confusion Matrix - Test data
p2 <- predict(rf, test)
confusionMatrix(p2, test$NSP)

# Error rate of Random Forest
plot(rf)

# Tune mtry
t <- tuneRF(train[-13], train[,13],
       stepFactor = 1,
       plot = TRUE,
       ntreeTry = 300,
       trace = TRUE,
       improve = 0.05)
