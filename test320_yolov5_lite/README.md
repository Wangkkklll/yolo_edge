## Environment Configuration
Raspberry Pi environment dependency configuration  
```
sudo apt-get install git cmake
sudo apt-get install -y gfortran
sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev libatlas-base-dev

```
## Ncnn Configuration and Compilation
```
$ git clone https://gitee.com/Tencent/ncnn.git
cd ncnn
mkdir build
cd build
cmake ..
make -j4
make install
```
## Onnx Convert
Convert e.onnx to fp16's last.param and last.bin files(Take input pixel 320 as an example)  
```
cd ncnn/build
./tools/onnx/onnx2ncnn e.onnx e.param e.bin 
./tools/ncnnoptimize e.param e.bin lite320.param lite320.bin 65536
```
## Compile
```
cd ncnn/build
cmake ..
make
```
After the compilation is complete, you can get an executable file
## Run
```
./lites320
```
