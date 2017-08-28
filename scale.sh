svm-scale -s scale 5fold/train$1.txt > train.scale
svm-scale -r scale 5fold/test$1.txt > test.scale
python tools/grid.py train.scale
