## 工具类脚本存放


### images 文件加内为图片处理

- 将某目录内图片全部转化成 500*500

```
python resize.py ./test/ 500
```

- 将某目录内图片随机切成 300*300

```
python randomCrop.py ./test/ 300
```


- 将某目录内图片类型转为RGB

```
python convertToRGB.py ./test/
```

- 将某目录内图片转为灰度图

```
python convertToL.py ./test/
```

- 将某目录内图片做二值化处理，其中阈值为 120。二值化图像每个像素用 8 个bit表示，0 表示黑，255 表示白。阈值的作用就是大于阈值为白，小于阈值为黑
在图像检测中较常用，可以去掉过多的干扰和噪点

```
python convertTo1.py ./test/ 120
```

- 将某张图片按照阈值 0~255 生成 256 张图片，用于选择合理的阈值

```
python getAllBinarizationImg.py test/github.JPG
```

- 将某目录内图片翻转 45 度，共翻转 7 次，每翻转一次生成一张图。适合增加样本数量。还在在翻转中随机增加剪裁、灰度等丰富样本数据 

```
python rotate.py test 45 7
```
