import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import scipy.ndimage

# Base directory = where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output folders (absolute paths!)
input_folder = os.path.join(base_dir, "Imfihlo isebhokisini")
output_folder = os.path.join(base_dir, "Imfihlo isebhokisini_final")
debug_folder = os.path.join(base_dir, "Imfihlo isebhokisini_debug")

# Make sure output & debug folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(debug_folder, exist_ok=True)

# Counter to keep pages in reading order
page_number = 1

# Choose a font (default system font if no TTF available)
try:
    font = ImageFont.truetype("arial.ttf", 60)  # adjust size if needed
except:
    font = ImageFont.load_default()

for file_name in sorted(os.listdir(input_folder)):
    if file_name.lower().endswith(".png"):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)

        # Get dimensions
        width, height = img.size

        # --- Improved spine detection using variance ---
        gray = img.convert("L")  # grayscale
        pixels = np.array(gray)

        center = width // 2
        search_range = 300  # pixels to look left/right of center
        left_bound = max(0, center - search_range)
        right_bound = min(width, center + search_range)

        spine_area = pixels[:, left_bound:right_bound]

        # Variance per column (text has high variance, spine is smoother)
        col_vars = spine_area.var(axis=0)

        # Smooth the variance profile to avoid noise
        smoothed = scipy.ndimage.gaussian_filter1d(col_vars, sigma=5)

        # Find column with lowest variance (most likely gutter)
        spine_index = smoothed.argmin()
        mid = left_bound + spine_index

        # --- Debug mode: draw line on original image ---
        debug_img = img.copy()
        draw_debug = ImageDraw.Draw(debug_img)
        draw_debug.line([(mid, 0), (mid, height)], fill="red", width=3)
        debug_img.save(os.path.join(debug_folder, f"debug_{file_name}"))

        # --- Split left and right pages ---
        left_page = img.crop((0, 0, mid, height))
        right_page = img.crop((mid, 0, width, height))

        # Add page numbers
        for page in [left_page, right_page]:
            draw = ImageDraw.Draw(page)
            text = f"Page {page_number}"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            x = page.width - text_w - 20
            y = page.height - text_h - 20
            draw.text((x, y), text, font=font, fill="black")

            # Save file
            page.save(os.path.join(output_folder, f"page_{page_number:04d}.png"))
            page_number += 1

print("✅ Done! Split and numbered pages saved in:", output_folder)
print("🔍 Debug images with red spine lines saved in:", debug_folder)
