svm-predict -b 1 train.scale train.scale.model Result_train.txt > result/5fold/Accuracy_train$1.txt
svm-predict -b 1 test.scale train.scale.model Result_test.txt > result/5fold/Accuracy_test$1.txt
