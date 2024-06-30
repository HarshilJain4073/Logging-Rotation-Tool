# Log Rotation Tool

This Python script automates log file rotation based on the size and number of files in a specified directory. It utilizes `os`, `sys`, `shutil`, `logging`, `gzip`, and `argparse` modules.

## Features

- **Log Directory Setup:**
  - Creates the specified log directory if it does not exist.
  - Handles user input to create the directory if necessary.

- **Rotation Criteria:**
  - Rotates log files based on maximum size (`max_size`) and maximum number of files (`max_file`).
  - Compresses logs exceeding `max_size` into gzip format and truncates the original file.
  - Removes older log files beyond `max_file` to maintain directory cleanliness.

- **Logging:**
  - Logs rotation actions, errors, and status updates using the `logging` module.
  - Configures logging to record timestamps, log levels, and messages to a `rotation.log` file within the specified directory.

## Usage

1. **Setup:**
   - Ensure Python 3.x and necessary modules (`os`, `sys`, `shutil`, `logging`, `gzip`, `argparse`) are installed.

2. **Command Line Arguments:**
   - `--log_dir`: Absolute path to the directory containing log files (required).
   - `--max_size`: Maximum size in bytes for each log file before rotation (default: 10 MB).
   - `--max_file`: Maximum number of log files to retain in the directory (default: 5).

3. **Running the Script:**
   - Execute the script with appropriate command line arguments:
     ```bash
     python log_rotation_tool.py --log_dir /path/to/logs --max_size 10485760 --max_file 5
     ```

4. **Output:**
   - Displays compression and removal actions taken.
   - Logs all operations to `rotation.log` in the specified `--log_dir`.

## Example

Assume `/path/to/logs` contains log files exceeding the configured limits:
  ```bash
  python log_rotation_tool.py --log_dir /path/to/logs --max_size 10485760 --max_file 5
  ```
## Output
    /path/to/logs 10485760 5
    Welcome to logging rotation tool
    Compressed /path/to/logs/logfile1.log
    Compressed /path/to/logs/logfile2.log
    /path/to/logs/logfile3.log.gz removed.
    Log rotation done.

Adjust configurations (max_size and max_file) based on your specific requirements and system capabilities.
