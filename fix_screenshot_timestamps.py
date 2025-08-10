#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Use current directory
directory = "."

# Filename formats for macOS screenshots:
# - macOS Mojave (10.14) and Later:
#   Screenshot YYYY-MM-DD at HH.MM.SS [AM|PM].png
# - Earlier macOS Versions (Before Mojave):
#   Screen Shot YYYY-MM-DD at HH.MM.SS.png

# Regex to match both old and new macOS screenshot filename formats
pattern = re.compile(
    r"^(Screen Shot|Screenshot) (\d{4})-(\d{2})-(\d{2}) at (\d{1,2})\.(\d{2})\.(\d{2})\s?(AM|PM)?\.png$"
)

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        _, year, month, day, hour, minute, second, ampm = match.groups()
        hour, minute, second = int(hour), int(minute), int(second)

        if ampm:
            ampm = ampm.upper()
            if ampm == "PM" and hour != 12:
                hour += 12
            elif ampm == "AM" and hour == 12:
                hour = 0

        dt = datetime(int(year), int(month), int(day), hour, minute, second)
        mod_time = dt.timestamp()

        file_path = os.path.join(directory, filename)
        access_time = os.stat(file_path).st_atime

        os.utime(file_path, (access_time, mod_time))

        print(f"✅ {filename} → {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"⚠️ Skipped: {filename}")
