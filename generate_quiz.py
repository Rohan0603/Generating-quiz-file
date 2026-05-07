import argparse
import csv
from pathlib import Path
from typing import List, Tuple

def read_quiz_data(filepath: Path) -> List[Tuple[str, str]]:
    """Reads quiz data from a CSV file.

    Args:
        filepath: The path to the CSV file.

    Returns:
        A list of tuples, where each tuple contains a question and its answer.
    """
    quiz_data = []
    with open(filepath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Skip header if present, or just read all rows if no header.
        # Let's assume the first row might be a header if it starts with "Question".
        first_row = next(reader, None)
        if first_row and first_row[0].lower() != 'question':
            quiz_data.append((first_row[0], first_row[1]))

        for row in reader:
            if len(row) >= 2:
                quiz_data.append((row[0], row[1]))
    return quiz_data

def generate_quiz_files(quiz_data: List[Tuple[str, str]], output_dir: Path) -> None:
    """Generates individual text files for each question and answer.

    Args:
        quiz_data: A list of tuples containing questions and answers.
        output_dir: The directory where the text files will be created.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, (question, answer) in enumerate(quiz_data, 1):
        question_file = output_dir / f"q{i}.txt"
        with open(question_file, 'w', encoding='utf-8') as qf:
            qf.write(f"Qno {i})\n{question}\n")

        answer_file = output_dir / f"a{i}.txt"
        with open(answer_file, 'w', encoding='utf-8') as af:
            af.write(f"{answer}\n")

def main() -> None:
    """Parses command line arguments and runs the quiz generation process."""
    parser = argparse.ArgumentParser(description="Generate quiz question and answer text files from a CSV.")
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input CSV file containing questions and answers."
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=Path("quiz_files"),
        help="Directory to output the generated text files (default: quiz_files)."
    )

    args = parser.parse_args()

    if not args.input_file.is_file():
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    quiz_data = read_quiz_data(args.input_file)
    if not quiz_data:
        print(f"Warning: No valid quiz data found in '{args.input_file}'.")
        return

    generate_quiz_files(quiz_data, args.output_dir)
    print(f"Successfully generated {len(quiz_data)} questions and answers in '{args.output_dir}'.")

if __name__ == "__main__":
    main()
