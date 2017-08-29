svm-scale -s scale $1/train$2.txt > train.scale
svm-scale -r scale $1/test$2.txt > test.scale
python tools/grid.py train.scale
