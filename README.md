# keras-yolo3


### Usage( inference)
Use --help to see usage of yolo_video.py:
```
usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                     [--input] [--output]
```

### Some issues to know
```
The test environment is
    - Python 3.8.8
    - Keras 2.1.5
    - tensorflow 1.6.0
```

### Training

1. Generate your own annotation file and class names file.  
    For VOC dataset, try `python voc_annotation.py`  
    Here is an example:
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```

2. Make sure you have run `python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5`  
    The file model_data/yolo_weights.h5 is used to load pretrained weights.

3. Modify train.py and start training.  
    `python train.py`  

### Training
logs/000/trained_weights_final.h5
set the above model to yolo.py after the training model.
