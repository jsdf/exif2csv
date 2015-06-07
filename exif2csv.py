import exifread
import csv
import os
import glob
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

tk_root = tk.Tk()
tk_root.withdraw()
input_dir = filedialog.askdirectory()
output_file = filedialog.asksaveasfilename(defaultextension='.csv', initialfile='image_exif_metadata')

# recursive glob
image_file_paths = glob.glob(os.path.join(input_dir, '*.*')) + glob.glob(os.path.join(input_dir, '*', '*.*'))

images_tags = []
for image_file_path in image_file_paths:
  # Open image file for reading (binary mode)
  f = open(image_file_path, 'rb')
  # get Exif tags
  images_tags.append(exifread.process_file(f, details=False))

exif_tag_types = sorted(images_tags[0].keys())
with open(output_file, 'w', encoding='utf8', newline='') as csvfile:
  c = csv.writer(csvfile)
  c.writerow(exif_tag_types)
  for tags in images_tags:
    row = []
    for exif_tag_type in exif_tag_types:
      tag_value = tags[exif_tag_type]
      if "DateTime" in exif_tag_type:
        tag_value = datetime.strptime(str(tag_value), '%Y:%m:%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
      row.append(tag_value)
    c.writerow(row)
