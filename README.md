# emotion-recognition
使用 [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) 辨識 [emo DB](http://emodb.bilderbar.info/docu/)

## 使用方法
1. 下載 [openSMILE](http://audeering.com/technology/opensmile/)
2. 解壓縮後並依照 document 進行編譯，將此資料夾放至 openSMILE-X.X.0 之中
3. 照順序執行 `script/oprnSmile.sh` , `script/convert.sh` , `script/main.py`
4. 
```
$ sh scale.sh $dir $index
$ sh train.sh $c $g
$ sh output.sh $dir $index
```

## 檔案說明
- `wav/` 從 eom DB 抓出來的音檔
- `arff/` 使用 openSMILE 的 IS09\_emotion.conf 提取的 feature
- `svm/` arff 處理後 libsvm 可以接受的類型
- `tools/` libsvm 提供的 python 工具
- `5fold/` `10fold/` 處理後的 test matrix 及 train matrix
- `result/` libsvm 跑出的辨識率結果
- `script/oprnSmile.sh` 將 `wav/` 中的音檔提取 feature
- `script/convert.sh` 呼叫 `arff2svm.py` 將 arff 檔案轉成 libsvm 接受格式
- `script/main.py` 將 `svm/` 中的檔案分為 5-fold 及 10-fold 需要的內容
- `scale.sh`, `output.sh` 的 `$index` 對應至 `$dir/` 中的檔案名稱編號
- `train.sh` 傳入 `scale.sh` 回傳的最佳參數
