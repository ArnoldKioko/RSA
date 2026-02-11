import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\realp\Downloads\image.png")
if image is None:
    raise ValueError("Failed to load image")

# --- Adjust these coordinates to match the Gamalink logo ---
# (x1, y1) = top-left corner
# (x2, y2) = bottom-right corner
x1, y1 = 193, 577
x2, y2 = 392, 691

# Draw white rectangle (redaction)
cv2.rectangle(
    image,
    (x1, y1),
    (x2, y2),
    (255, 255, 255),
    thickness=-1
)

# Save output
cv2.imwrite(
    r"C:\Users\realp\Downloads\certificate_white_bg.png",
    image
)

print("Saved: certificate_white_bg.png")
