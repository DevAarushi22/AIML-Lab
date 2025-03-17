# Face Prediction using YOLO

## Overview
This project implements face prediction using the YOLO (You Only Look Once) object detection model. The model is trained to detect and predict faces in images and video streams with high accuracy and speed.

## Features
- Real-time face detection using YOLO.
- Works with images and video streams.
- Fast and accurate detection.
- Easy to use and extend for other face-related applications.

## Requirements
To run this project, you need the following dependencies:

```bash
pip install opencv-python numpy torch torchvision yolov5
```

Other dependencies can be found in the `requirements.txt` file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/face-prediction-yolo.git
   cd face-prediction-yolo
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the YOLO model weights:
   ```bash
   wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt
   ```

## Usage
### Face Prediction on an Image
```bash
python detect.py --source image.jpg --weights yolov5s.pt --conf 0.4 --classes 0
```

### Face Prediction on a Video
```bash
python detect.py --source video.mp4 --weights yolov5s.pt --conf 0.4 --classes 0
```

### Real-time Face Prediction using Webcam
```bash
python detect.py --source 0 --weights yolov5s.pt --conf 0.4 --classes 0
```

## Customization
- Modify `conf` (confidence threshold) for detection accuracy.
- Adjust `weights` to use different YOLO models (e.g., `yolov5m.pt`, `yolov5l.pt`).
- To train on a custom dataset, follow YOLO's official training guide.

## Results
The detected faces will be displayed with bounding boxes. The processed images/videos are saved in the `runs/detect/` directory.

## References
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)

## License
This project is open-source and available under the MIT License.

## Author
Aarushi

