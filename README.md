# A Cascaded Inception of Inception Network with Attention Modulated Feature Fusion for Human Pose Estimation
Wentao Liu, Jie Chen, Cheng Li, Chen Qian, Xiao Chu, Xiaolin Hu, "[A Cascaded Inception of Inception Network with Attention Modulated Feature Fusion for Human Pose Estimation](https://ojs.aaai.org/index.php/AAAI/article/view/12334)", AAAI 2018.


![Teaser?](https://github.com/LiuwtWinter/Cascaded-Inception-of-Inception/blob/master/Images/Framework.png)

## Install dependency library
-  Install [CPM](https://github.com/shihenw/convolutional-pose-machines-release).
- Compile Caffe inside CPM and make sure that you have compiled python as well.

## Add layers to caffe
- We add Interp and BN layers into the CPM caffe version following the implementation of [PSPNet](https://github.com/hszhao/PSPNet)
- Please add the layers as follow:
  - Clone caffe from the [PSPNet](https://github.com/hszhao/PSPNet)
  - Replace the [caffe.proto](https://github.com/shihenw/caffe/blob/d154e896b48e8fb520cb4b47af8ba10bf9403382/src/caffe/proto/caffe.proto) file by the one in this repo.
- Add the following files into the specific directories
  - caffe/include/caffe/
    - [common.cuh](https://github.com/hszhao/PSPNet/blob/master/include/caffe/common.cuh)

  - caffe/include/caffe/layers/
    - [interp_layer.hpp](https://github.com/hszhao/PSPNet/blob/master/include/caffe/layers/interp_layer.hpp)
    - [bn_layer.hpp](https://github.com/hszhao/PSPNet/blob/master/include/caffe/layers/bn_layer.hpp)
  - caffe/include/caffe/util/
    - [interp.hpp](https://github.com/hszhao/PSPNet/blob/master/include/caffe/util/interp.hpp)
  - caffe/src/caffe/layers/
    - [interp_layer.cpp](https://github.com/hszhao/PSPNet/blob/master/src/caffe/layers/interp_layer.cpp)
    - [bn_layer.cpp](https://github.com/hszhao/PSPNet/blob/master/src/caffe/layers/bn_layer.cpp)
    - [bn_layer.cu](https://github.com/hszhao/PSPNet/blob/master/src/caffe/layers/bn_layer.cu)
  - caffe/src/caffe/util/
    - [interp.cpp](https://github.com/hszhao/PSPNet/blob/master/src/caffe/util/interp.cpp)
    - [interp.cu](https://github.com/hszhao/PSPNet/blob/master/src/caffe/util/interp.cu)
- Recompile caffe 

## Model Setup
- Copy the model in this repo to cpm_root/convolutional-pose-machines-release/model/
- Copy the provided files into cpm_root/convolutional-pose-machines-release/testing/python/
  -  [config_reader.py](https://github.com/LiuwtWinter/Cascaded-Inception-of-Inception/blob/master/Model%20setup/config_reader.py)
  -  [config_AIOI](https://github.com/LiuwtWinter/Cascaded-Inception-of-Inception/blob/master/Model%20setup/config_AIOI)

## Testing  
- Use the [code](https://github.com/shihenw/convolutional-pose-machines-release/blob/master/testing/python/demo.ipynb) provided by CPM to evaluate the model
- Replace the pose estimation inference code with the provided [Inference.py](https://github.com/LiuwtWinter/Cascaded-Inception-of-Inception/blob/master/Testing/Inference.py) in this repo
   
## Citation
Please cite:

    @inproceedings{liu2018cascaded,
            author={Liu, Wentao and Chen, Jie and Li, Cheng and Qian, Chen and Chu, Xiao and Hu, Xiaolin},
            title={A cascaded inception of inception network with attention modulated feature fusion for human pose estimation},
            booktitle={Thirty-second AAAI conference on artificial intelligence},
            year={2018}
    }

