# NeoMate

NeoMate is a Python program designed to quickly change file attributes such as read-only, hidden, or system across multiple files on Windows. This tool is especially useful for managing file permissions and visibility in bulk.

## Features

- Modify multiple files at once.
- Set or unset the read-only attribute.
- Set or unset the hidden attribute.
- Set or unset the system attribute.

## Requirements

- Python 3
- Windows Operating System

## Installation

1. Clone the repository or download the `NeoMate.py` file.
2. Ensure you have Python 3 installed on your system.

## Usage

Open a command prompt or terminal and navigate to the directory containing `NeoMate.py`. Use the following syntax to change file attributes:

```bash
python NeoMate.py [options] file1 file2 ...
```

### Options

- `--read-only`: Set the files to read-only.
- `--no-read-only`: Unset the read-only attribute.
- `--hidden`: Set the files to hidden.
- `--no-hidden`: Unset the hidden attribute.
- `--system`: Set the files to system.
- `--no-system`: Unset the system attribute.

### Example

To set the read-only and hidden attributes for multiple files:

```bash
python NeoMate.py --read-only --hidden file1.txt file2.txt
```

To unset the system attribute for a single file:

```bash
python NeoMate.py --no-system file1.txt
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit a pull request or open an issue to contribute to this project.