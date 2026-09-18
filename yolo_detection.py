# yolo_detection.py

from ultralytics import YOLO

from config import (
    MODEL_PATH,
    CONFIDENCE,
    IMAGE_SIZE
)


print("Loading YOLO model...")

model = YOLO(MODEL_PATH)

print("YOLO model loaded.")


def detect_droplets(image):

    print("Running YOLO detection...")

    results = model.predict(
        source=image,
        conf=CONFIDENCE,
        imgsz=IMAGE_SIZE,
        verbose=False
    )

    result = results[0]

    droplets = []

    if result.boxes is None:
        return droplets

    for box in result.boxes:

        x1, y1, x2, y2 = (
            box.xyxy[0]
            .cpu()
            .numpy()
        )

        confidence = float(
            box.conf[0]
        )

        class_id = int(
            box.cls[0]
        )

        class_name = result.names[
            class_id
        ]

        center_x = (
            x1 + x2
        ) / 2

        center_y = (
            y1 + y2
        ) / 2

        droplets.append({
            "class_name": class_name,

            "confidence": confidence,

            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2),

            "center_x": float(center_x),
            "center_y": float(center_y),

            "well": None
        })

    return droplets