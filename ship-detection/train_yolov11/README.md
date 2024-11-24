# Quick start

1. Install ultralytics pip package using `pip install ultralytics`
2. Make sure current directory is opened in terminal during training
3. Do next steps for dataset model is planned to be trained on

## Sentinel-1 dataset (sattelite images)
1. Prepare the data 
   1. Download and unzip to the current directory the `SAR-Ship-Dataset` from https://github.com/CAESAR-Radi/SAR-Ship-Dataset
   2. Run `python3 prepare_sar_ship_dataset.py` file, it should create file `sar-ships.yaml`
2Train the YOLOv11 on Sentinel-1 data
   1. Using YOLO CLI: `yolo detect train data=sar-ships.yaml model=yolo11n.yaml epochs=100 imgsz=640`
   2. Using Python: `python3 train.py sar-ships.yaml`

## HRSC2016-MS dataset (drone images)
1. Prepare the data 
   1. Download and unzip to the current directory the `HRSC2016-MS` from https://datasetninja.com/hrsc2016-ms
   2. Run `python3 prepare_hrsc2016_ms_dataset.py` file, it should create file `hrsc2016-ms.yaml`
2. Train the YOLOv11 on HRSC2016-MS data
   1. Using YOLO CLI: `yolo detect train data=hrsc2016-ms.yaml model=yolo11n.yaml epochs=100 imgsz=640`
   2. Using Python: `python3 train.py hrsc2016-ms.yaml`
