# calibrate_wells.py

import cv2

from camera_capture import capture_frame


print()
print("============================")
print("DMF WELL CALIBRATION")
print("============================")
print()

print(
    "You will draw one box around each well."
)

print(
    "For every well:"
)

print(
    "Drag the rectangle and press ENTER."
)

print()


image = capture_frame()

height, width = image.shape[:2]

well_regions = {}


for well_number in range(1, 9):

    print(
        f"Select WELL {well_number}"
    )

    x, y, w, h = cv2.selectROI(
        f"Select Well {well_number}",
        image,
        showCrosshair=True,
        fromCenter=False
    )

    cv2.destroyAllWindows()

    if w == 0 or h == 0:

        print(
            f"Well {well_number} was skipped."
        )

        continue


    left = x / width
    top = y / height

    right = (
        x + w
    ) / width

    bottom = (
        y + h
    ) / height


    well_regions[
        well_number
    ] = (

        left,
        top,
        right,
        bottom

    )


print()
print("============================")
print("COPY THIS INTO config.py")
print("============================")
print()

print("WELL_REGIONS = {")


for well_number, region in well_regions.items():

    left, top, right, bottom = region

    print(
        f"    {well_number}: "
        f"({left:.6f}, "
        f"{top:.6f}, "
        f"{right:.6f}, "
        f"{bottom:.6f}),"
    )


print("}")