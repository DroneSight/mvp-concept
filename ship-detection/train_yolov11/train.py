from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('data', type=str, help='Path to yaml file with training configuration')
args = parser.parse_args()


# Load a model, for demo purposes we use a small version of YOLOv11
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data=args.data,
    epochs=100
)