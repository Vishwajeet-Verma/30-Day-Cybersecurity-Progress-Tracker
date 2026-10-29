# System Information Script

A beginner-friendly Python project that collects basic system information.

## Features

- Hostname and current username
- Operating system and kernel version
- Local IP address
- Disk usage
- Memory usage
- Safe handling of selected system commands

## Requirements

- Python 3
- Linux or WSL recommended

## How to Run

```bash
python3 system_info.py
```

## Project Files

- `system_info.py` — Main Python script
- `sample_output.txt` — Example program output

## Security

The script uses an allowlist for selected system commands and executes them without a shell. This is a basic safety measure, not a complete security sandbox.

## Limitations

- Results may differ between Linux, WSL and Windows.
- IP address detection depends on network configuration.
- Disk and memory information may not represent the entire physical computer in a virtualized environment.
- The script is intended for basic learning and system inspection, not a full security audit.

## Learning Objectives

Practice Python functions, system libraries, error handling, subprocess usage and documentation.
