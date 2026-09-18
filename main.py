# main.py

import cv2

from pathlib import Path
from datetime import datetime

from camera_capture import capture_frame

from yolo_detection import (
    detect_droplets
)

from well_mapping import (
    find_well,
    draw_wells
)

from config import CAPTURE_FOLDER


print()
print("==============================")
print("DMF DROPLET VISION")
print("==============================")
print()


# ==============================
# STEP 1
# TAKE PHOTO
# ==============================

image = capture_frame()

image_height, image_width = (
    image.shape[:2]
)

print(
    f"Image size: "
    f"{image_width} x {image_height}"
)


# ==============================
# STEP 2
# RUN YOLO
# ==============================

droplets = detect_droplets(
    image
)


# ==============================
# STEP 3
# FIND WELL FOR EACH DROPLET
# ==============================

for droplet in droplets:

    droplet["well"] = find_well(

        droplet["center_x"],
        droplet["center_y"],

        image_width,
        image_height
    )


# ==============================
# STEP 4
# CREATE MARKED IMAGE
# ==============================

annotated = image.copy()


# Draw Well 1 through Well 8
annotated = draw_wells(

    annotated,
    image_width,
    image_height

)


# Draw YOLO results
for droplet in droplets:

    x1 = int(
        droplet["x1"]
    )

    y1 = int(
        droplet["y1"]
    )

    x2 = int(
        droplet["x2"]
    )

    y2 = int(
        droplet["y2"]
    )


    center_x = int(
        droplet["center_x"]
    )

    center_y = int(
        droplet["center_y"]
    )


    confidence = (
        droplet["confidence"]
    )

    well = (
        droplet["well"]
    )


    # Draw droplet bounding box
    cv2.rectangle(
        annotated,
        (x1, y1),
        (x2, y2),

        (0, 255, 0),
        3
    )


    # Draw droplet center
    cv2.circle(
        annotated,

        (
            center_x,
            center_y
        ),

        6,

        (0, 0, 255),

        -1
    )


    if well is not None:

        label = (
            f"Droplet -> Well {well} "
            f"({confidence:.2f})"
        )

    else:

        label = (
            f"Droplet -> Outside wells "
            f"({confidence:.2f})"
        )


    cv2.putText(
        annotated,

        label,

        (
            x1,
            max(
                y1 - 10,
                25
            )
        ),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.65,

        (0, 255, 0),

        2
    )


# ==============================
# STEP 5
# PRINT RESULTS
# ==============================

print()
print("==============================")
print("RESULTS")
print("==============================")
print()


print(
    f"Total droplets detected: "
    f"{len(droplets)}"
)


print()


for number, droplet in enumerate(
    droplets,
    start=1
):

    print(
        f"Droplet {number}"
    )

    print(
        f"  Well: "
        f"{droplet['well']}"
    )

    print(
        f"  Confidence: "
        f"{droplet['confidence']:.3f}"
    )

    print(
        f"  Position: "
        f"({droplet['center_x']:.1f}, "
        f"{droplet['center_y']:.1f})"
    )

    print()


# ==============================
# WELL SUMMARY
# ==============================

print("------------------------------")
print("WELL SUMMARY")
print("------------------------------")


occupied_wells = []


for well_number in range(
    1,
    9
):

    count = sum(

        1

        for droplet in droplets

        if droplet["well"]
        == well_number

    )


    if count > 0:

        occupied_wells.append(
            well_number
        )


    print(
        f"Well {well_number}: "
        f"{count} droplet(s)"
    )


print()

print(
    "Occupied wells:",
    occupied_wells
)


# ==============================
# SAVE IMAGES
# ==============================

Path(
    CAPTURE_FOLDER
).mkdir(
    exist_ok=True
)


timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)


raw_path = (
    f"{CAPTURE_FOLDER}/"
    f"raw_{timestamp}.jpg"
)


result_path = (
    f"{CAPTURE_FOLDER}/"
    f"result_{timestamp}.jpg"
)


cv2.imwrite(
    raw_path,
    image
)


cv2.imwrite(
    result_path,
    annotated
)


print()
print(
    f"Result image saved to:"
)

print(
    result_path
)


# ==============================
# SHOW RESULT
# ==============================

cv2.imshow(
    "DMF Droplet Detection",
    annotated
)


print()
print(
    "Look at the image and confirm "
    "the detections/well assignments."
)

print(
    "Press any key while the image "
    "window is selected to close."
)


cv2.waitKey(0)

cv2.destroyAllWindows()