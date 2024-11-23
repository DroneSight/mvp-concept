# Quick start

1. Install ultralytics pip package using `pip install ultralytics`
2. Make sure current directory is opened in terminal during training
3. Prepare the data 
   1. Download and unzip to the current directory the `SAR-Ship-Dataset` from https://github.com/CAESAR-Radi/SAR-Ship-Dataset
   2. Run `python3 prepare_sar_ship_dataset.py` file, it should create file `sar-ships.yaml`
4. Train the YOLOv11 on Sentinel-1 data
   1. Using YOLO CLI: `yolo detect train data=sar-ships.yaml model=yolo11n.yaml epochs=100 imgsz=640`
   2. Using Python: `python3 train.py sar-ships.yaml`
