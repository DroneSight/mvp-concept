from ultralytics import YOLO

# Load a model, for demno purposes we use a small version of YOLOv11
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="config.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
)