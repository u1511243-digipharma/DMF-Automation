# camera_capture.py

import cv2

from config import (
    CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT,
    CAMERA_WARMUP_FRAMES
)


def capture_frame():

    print("Opening Logitech camera...")

    # Windows webcam connection
    camera = cv2.VideoCapture(
        CAMERA_INDEX,
        cv2.CAP_DSHOW
    )

    # Backup method if DirectShow fails
    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(CAMERA_INDEX)

    if not camera.isOpened():
        raise RuntimeError(
            "Could not open the camera. "
            "Try CAMERA_INDEX = 1 or 2 in config.py. "
            "Also make sure MicroDrop is not locking the webcam."
        )

    camera.set(
        cv2.CAP_PROP_FRAME_WIDTH,
        CAMERA_WIDTH
    )

    camera.set(
        cv2.CAP_PROP_FRAME_HEIGHT,
        CAMERA_HEIGHT
    )

    # Let exposure/focus settle
    for _ in range(CAMERA_WARMUP_FRAMES):
        camera.read()

    success, frame = camera.read()

    camera.release()

    if not success:
        raise RuntimeError(
            "Camera opened, but could not capture an image."
        )

    print("Image captured.")

    return frame