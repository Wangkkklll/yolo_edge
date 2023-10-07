# <p align="center"> YOLO_EDGE🚀</p>

<p align="center"><img src="https://img.shields.io/badge/YOLO~EDGE-v0.1-red?logo=gitlab&style=for-the-badge"> <img src="https://img.shields.io/badge/license-MIT-blue?logo=Hexo&style=for-the-badge"> </p>

## Introduction 
1、本项目是基于目标检测算法的车载辅助系统，同时具备检测行人与路面缺陷的能力  
2、所部署的硬件设备为树莓派4B  
3、具体的实现效果可参考[bilibili视频演示](https://www.bilibili.com/video/BV1EV411M7fK/?spm_id_from=333.999.0.0)

## Usage
1、模型的训练  
使用的模型为yolov5与yolov5-lite，具体训练的流程与权重参考[YOLOv5-Lite下的README文档](https://github.com/Wangkkklll/yolo_edge/tree/main/YOLOv5-Lite-)  
  
2、模型的部署  
部署采用的框架为NCNN，具体步骤参考[test320_yolov5_lite下的README文档](https://github.com/Wangkkklll/yolo_edge/tree/main/test320_yolov5_lite)  

3、路面缺陷检测结果可视化  
首先通过GPS读取坐标，并调用高德地图API进行标记，具体参考[可视化代码使用文档]()  

4、测距模块  
测距模块分为超声测距与视觉测距，具体参考[测距模块文档]()

## 参考项目
<div id="refer-id"></div>
[1]Xiangrong Chen, & Ziman Gong. YOLOv5-Lite: Lighter, faster and easier to deploy.


