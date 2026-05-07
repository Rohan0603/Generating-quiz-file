# Quiz Generator

This script generates individual question and answer text files from a source CSV file.

## Features
- Reads questions and answers robustly from a CSV format.
- Uses `argparse` for easy command-line configuration.
- Automatically creates an output directory for the generated files (defaults to `quiz_files/`).

## Requirements
- Python 3.6+

## Usage
Run the script using Python, passing the input CSV file as a positional argument. By default, it outputs files into `quiz_files/`.

```bash
python3 generate_quiz.py quiz.csv
```

To output the files to a custom directory:
```bash
python3 generate_quiz.py quiz.csv -o my_custom_directory
```

## Input Format
The script expects a CSV file containing at least two columns: Question and Answer. If the first row is a header starting with "Question", it will be skipped.

```csv
Question,Answer
"What is 2 + 2?","4"
"Who wrote Hamlet?","William Shakespeare"
```
