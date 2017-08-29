svm-predict -b 1 train.scale train.scale.model result/$1/Result_train$2.txt > accuracy/$1/Accuracy_train$2.txt
svm-predict -b 1 test.scale train.scale.model result/$1/Result_test$2.txt > accuracy/$1/Accuracy_test$2.txt
