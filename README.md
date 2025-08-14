# macOS Screenshot Timestamps

A small Python script to **synchronize the file modification date** of macOS screenshots with the timestamp embedded in their filename.

## Features

- Supports both `Screen Shot` and `Screenshot` macOS screenshot filename formats.
- Handles AM/PM time format.
- Supports both regular and non-breaking spaces before the AM/PM suffix.
- Preserves the original file access time.
- Prints a clear summary of processed and skipped files.

## Supported Filename Patterns

| Example Filename                                   | Notes                            |
|--------------------------------------------------|---------------------------------|
| `Screen Shot 2020-08-08 at 13.37.00.png`         | Uses 24-hour format             |
| `Screenshot 2025-08-10 at 2.23.05 PM.png`        | Uses 12-hour format with AM/PM  |

## Usage

```bash
python3 fix_screenshot_timestamps.py [directory]
```

- If `[directory]` is provided, the script searches for screenshots in the given directory.
- If omitted, it searches in the current working directory.
- It updates the **modification time** to match the timestamp found in the filename.

## Requirements

- Python **3.6+**
- Read and write access to the target directory

## Example Output

```
✅ Screen Shot 2018-01-30 at 16.47.27.png → 2018-01-30 16:47:27
✅ Screen Shot 2023-03-31 at 9.59.34 AM.png → 2023-03-31 09:59:34
✅ Screenshot 2025-05-27 at 11.13.56 PM.png → 2025-05-27 23:13:56
✅ Screenshot 2025-08-10 at 10.15.30 AM.png → 2025-08-10 10:15:30
⚠️ Skipped: foobar.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
