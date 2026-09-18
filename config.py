# config.py

# =========================
# CAMERA SETTINGS
# =========================

CAMERA_INDEX = 0

CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1080

CAMERA_WARMUP_FRAMES = 20


# =========================
# YOLO SETTINGS
# =========================

MODEL_PATH = "Models/dmf_v1.pt"

# Your current model works well around this value
CONFIDENCE = 0.05

IMAGE_SIZE = 640


# =========================
# OUTPUT
# =========================

CAPTURE_FOLDER = "captures"


# =========================
# WELL LOCATIONS
# =========================
#
# You will replace these after running:
#
#     python calibrate_wells.py
#
# Format:
#
# well_number: (left, top, right, bottom)
#
# Coordinates are normalized from 0 to 1.

WELL_REGIONS = {
    1: (0.10, 0.10, 0.20, 0.30),
    2: (0.20, 0.10, 0.30, 0.30),
    3: (0.30, 0.10, 0.40, 0.30),
    4: (0.40, 0.10, 0.50, 0.30),

    5: (0.10, 0.60, 0.20, 0.80),
    6: (0.20, 0.60, 0.30, 0.80),
    7: (0.30, 0.60, 0.40, 0.80),
    8: (0.40, 0.60, 0.50, 0.80),
}