from ultralytics import YOLO

# Load a model

if __name__ == "__main__":
  # Use the model
  model = YOLO("yolov8s.yaml")  # build a new model from scratch
  results = model.train(data="config.yaml", epochs=200,imgsz=256,optimizer="Adam", device='0')  # train the model
