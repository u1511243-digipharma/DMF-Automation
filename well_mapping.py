# well_mapping.py

import cv2

from config import WELL_REGIONS


def find_well(
    center_x,
    center_y,
    image_width,
    image_height
):

    # Convert pixel location into 0-1 coordinates
    normalized_x = (
        center_x / image_width
    )

    normalized_y = (
        center_y / image_height
    )

    for well_number, region in WELL_REGIONS.items():

        left, top, right, bottom = region

        if (
            left <= normalized_x <= right
            and
            top <= normalized_y <= bottom
        ):

            return well_number

    return None


def draw_wells(
    image,
    image_width,
    image_height
):

    for well_number, region in WELL_REGIONS.items():

        left, top, right, bottom = region

        x1 = int(
            left * image_width
        )

        y1 = int(
            top * image_height
        )

        x2 = int(
            right * image_width
        )

        y2 = int(
            bottom * image_height
        )

        # Draw well boundary
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (255, 255, 0),
            2
        )

        # Label well
        cv2.putText(
            image,
            f"Well {well_number}",
            (x1 + 5, y1 + 25),

            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,

            (255, 255, 0),
            2
        )

    return image