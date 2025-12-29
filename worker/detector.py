import cv2
from ultralytics import YOLO

model = YOLO("yolov5su.pt")  # COCO, klasa 0 = person


def detect_people(image_path, output_path):
    img = cv2.imread(image_path)
    results = model(img)

    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # person
                count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(
                    img,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

    cv2.imwrite(output_path, img)
    return count
