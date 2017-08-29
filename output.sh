svm-predict -b 1 train.scale train.scale.model Result_train.txt > result/$1/Accuracy_train$2.txt
svm-predict -b 1 test.scale train.scale.model Result_test.txt > result/$1/Accuracy_test$2.txt
