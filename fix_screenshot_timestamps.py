#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Use current directory
directory = "."

# Regex pattern matches both "Screen Shot" and "Screenshot" formats, ending in .png
pattern = re.compile(r"(Screen Shot|Screenshot) (\d{4})-(\d{2})-(\d{2}) at (\d{2})\.(\d{2})\.(\d{2})\.png$")

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        _, year, month, day, hour, minute, second = match.groups()
        dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
        mod_time = dt.timestamp()

        file_path = os.path.join(directory, filename)

        # Preserve current access time
        current_access_time = os.stat(file_path).st_atime

        # Update only the modification time
        os.utime(file_path, (current_access_time, mod_time))

        print(f"✅ Updated modification time: {filename} → {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"⚠️ Skipped (name pattern not matched): {filename}")
