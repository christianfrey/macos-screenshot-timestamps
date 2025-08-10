# macOS Screenshot Timestamps

A small Python script to **synchronize the file modification date** of macOS screenshots with the timestamp embedded in their filename.

## Features

- Supports both legacy (`Screen Shot`) and modern (`Screenshot`) macOS screenshot filename formats.
- Handles AM/PM time format used in recent macOS versions.
- Preserves the original file access time.
- Prints a clear summary of processed and skipped files.

## Supported Filename Patterns

| macOS Version          | Example Filename                                   | Notes                            |
|------------------------|----------------------------------------------------|-----------------------------------|
| Pre-Mojave (≤ 10.13)   | `Screen Shot 2025-08-10 at 13.37.07.png`            | Uses 24-hour format               |
| Mojave (10.14) and later | `Screenshot 2025-08-10 at 2.23.05 PM.png`         | Uses 12-hour format with AM/PM    |

## Usage

```bash
python3 fix_screenshot_timestamps.py
```

* The script currently uses the current working directory (.) to search for screenshots.
* The script updates the **modification time** to match the date and time found in the filename.

## Requirements

* Python **3.6+**
* Read and write access to the target directory

## Example Output

```
✅ Screenshot 2025-08-10 at 10.15.30 AM.png → 2025-08-10 10:15:30
⚠️ Skipped: foobar.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

