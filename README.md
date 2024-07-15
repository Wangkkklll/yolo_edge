# <p align="center"> YOLO_EDGE🚀</p>
### News 
**2024-07-14** The usage guidelines will be improved within this month.  
**2023-10-06**  We released code and pre-trained model.
<p align="center"><img src="https://img.shields.io/badge/YOLO~EDGE-v0.1-red?logo=gitlab&style=for-the-badge"> <img src="https://img.shields.io/badge/license-MIT-blue?logo=Hexo&style=for-the-badge"> </p>

## Introduction 
1、This project is an on-board assistance system based on target detection algorithm, which also has the ability to detect pedestrians and road defects.  
2、The deployed hardware device is Raspberry Pi 4B.  
3、The specific implementation effect is [bilibili video](https://www.bilibili.com/video/BV1EV411M7fK/?spm_id_from=333.999.0.0)

## Usage
1、Model Training  
The models used are yolov5 and yolov5-lite. For the specific training process, refer to [YOLOv5-Lite: README.md](https://github.com/Wangkkklll/yolo_edge/tree/main/YOLOv5-Lite)  
  
2、Model deployment  
The framework used for deployment is NCNN. For specific steps, refer to [test320_yolov5_lite: README.md](https://github.com/Wangkkklll/yolo_edge/tree/main/test320_yolov5_lite)  

3、Visualization  
Read the coordinates through GPS and call the Amap API to mark them. For details, refer to [Visualization](https://github.com/Wangkkklll/yolo_edge/tree/main/YOLOv5-Lite)  

4、Distance measurement module  
The ranging module is divided into ultrasonic ranging and visual ranging. For details, please refer to [Distance](https://github.com/Wangkkklll/yolo_edge/tree/main/YOLOv5-Lite)
## Contact us
kangliwang@stu.pku.edu.cn
## Ref
[1] Xiangrong Chen, & Ziman Gong. YOLOv5-Lite: Lighter, faster and easier to deploy.

[2] https://github.com/ultralytics/yolov5

[3] https://github.com/Tencent/ncnn


