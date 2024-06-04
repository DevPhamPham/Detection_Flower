import os
import cv2
from ultralytics import YOLO
import time

# Đường dẫn tới video và định dạng đầu ra
VIDEOS_DIR = '.'
video_path = os.path.join(VIDEOS_DIR, 'predict.mp4')
video_path_out = '{}_out.mp4'.format("predict")

# Khởi tạo VideoCapture và VideoWriter
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Danh sách các lớp
classes = ["Hoa Dao", "Hoa Mai"]

# Đường dẫn đến tệp best.pt của mô hình YOLO
model_path = "./runs/detect/train3/weights/best.pt"

# Load mô hình YOLO
model = YOLO(model_path)

threshold = 0.1

while ret:
    results = model(frame)[0]

    for pred in results.boxes.data.tolist():
        x1, y1, x2, y2 = map(int, pred[:4])
        score = round(float(pred[4]),2)
        class_id = int(pred[5])

        if score > threshold:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
            cv2.putText(frame, classes[class_id].upper() + " " + str(score), (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
