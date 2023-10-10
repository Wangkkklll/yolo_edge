# <p align="center"> YOLO_EDGE🚀</p>

<p align="center"><img src="https://img.shields.io/badge/YOLO~EDGE-v0.1-red?logo=gitlab&style=for-the-badge"> <img src="https://img.shields.io/badge/license-MIT-blue?logo=Hexo&style=for-the-badge"> </p>

# data prepare
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要实现行人检测与路面缺陷检测，需要对这两类样本进行标注。本项目采用COCO数据集提取行人样本，RDD2022数据集提取路面缺陷样本。最终处理得到**65535**个行人数据集与**38385**个路面缺陷数据集。
而对于合并后的数据集的异常样本:**部分道路缺陷的数据集中存在行人，但是在合并过程中，是没有这部分行人的数据的，因此这些数据的存在对模型的训练的精度的影响非常大**。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们进行了手动剔除，如下所示：  
![image](https://github.com/Wangkkklll/yolo_edge/assets/71534709/ee6f6fb8-3699-4001-8678-528207ff9d72)



# data open
本项目将公开我们处理好的数据集，整理后会挂到以下[网址]()  
