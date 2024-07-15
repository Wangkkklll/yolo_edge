# <p align="center"> YOLO_EDGE🚀</p>

<p align="center"><img src="https://img.shields.io/badge/YOLO~EDGE-v0.1-red?logo=gitlab&style=for-the-badge"> <img src="https://img.shields.io/badge/license-MIT-blue?logo=Hexo&style=for-the-badge"> </p>

## Data prepare
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To achieve pedestrian detection and road defect detection, these two types of samples need to be labeled. This project uses the COCO dataset to extract pedestrian samples and the RDD2022 dataset to extract road defect samples. The final processing results are **65535** pedestrian datasets and **38385** road defect datasets.
As for the abnormal samples of the merged dataset: **there are pedestrians in some road defect datasets, but there is no data of these pedestrians in the merging process, so the existence of these data has a great impact on the accuracy of model training**。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
![image](https://github.com/Wangkkklll/yolo_edge/assets/71534709/ee6f6fb8-3699-4001-8678-528207ff9d72)

!Note that due to time constraints, some data may not be cleaned. We did not explore whether the detection performance was greatly affected.
## Data open
Dataset Download：[Pedestrian and road surface defect dataset](https://pan.baidu.com/s/1Ds02DxrUHpb_0lvD5NVRQA?pwd=kkll )  

## <div>How to use</div>

<details open>
<summary>Install</summary>

[**Python>=3.6.0**](https://www.python.org/) is required with all
[requirements.txt](https://github.com/ppogg/YOLOv5-Lite/blob/master/requirements.txt) installed including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/Wangkkklll/yolo_edge.git
$ cd yolo_edge/YOLOv5-Lite
$ pip install -r requirements.txt
```

</details>

<details>
<summary>Inference with detect.py</summary>

`detect.py` runs inference on a variety of sources, downloading models automatically from
the [latest YOLOv5-Lite release](https://github.com/ppogg/YOLOv5-Lite/releases) and saving results to `runs/detect`.

```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

</details>

<details open>
<summary>Training</summary>

```bash
$ python train.py --data data.yaml --cfg v5lite-e.yaml --weights v5lite-e.pt --batch-size 128
                                         v5lite-s.yaml           v5lite-s.pt              128
                                         v5lite-c.yaml           v5lite-c.pt               96
                                         v5lite-g.yaml           v5lite-g.pt               64
```

 If you use multi-gpu. It's faster several times:
  
 ```bash
$ python -m torch.distributed.launch --nproc_per_node 2 train.py
```
  
</details>  

</details>

<details open>
<summary>DataSet</summary>

Training set and test set distribution （the path with xx.jpg）
  
 ```bash
train: ../dataset/images/train/
val: ../dataset/images/val/
```
```bash
├── images            # xx.jpg example
│   ├── train        
│   │   ├── 000001.jpg
│   │   ├── 000002.jpg
│   │   └── 000003.jpg
│   └── val         
│       ├── 100001.jpg
│       ├── 100002.jpg
│       └── 100003.jpg
└── labels             # xx.txt example      
    ├── train       
    │   ├── 000001.txt
    │   ├── 000002.txt
    │   └── 000003.txt
    └── val         
        ├── 100001.txt
        ├── 100002.txt
        └── 100003.txt
```
  
</details> 
<details open>
<summary>Export Model</summary>
  
Export onnx file and simplify  
```
python export.py --weights weights/best.pt
python -m onnxsim best.onnx e.onnx
```

</details> 
