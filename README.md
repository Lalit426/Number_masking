# Number Masking Project

A simple Python project that reads employee data from a text file, identifies 10-digit mobile numbers using Regular Expressions, and displays their masked versions.

## Features

- Reads employee data from a text file
- Finds 10-digit mobile numbers using Regular Expressions
- Displays the original number and its masked version
- Helps understand basic data masking concepts
- Uses Python file handling and Regex

## Technologies Used

- Python
- File Handling
- Regular Expressions (Regex)

## How It Works

The program reads data from an employee data file and uses `re.findall()` to find 10-digit numbers.

Each identified mobile number is then replaced with `xxxxxxxxxx` to create a masked version.

The program displays the result in the following format:

Original Number : Masked Number

9876543210 : xxxxxxxxxx

## Example

Input:

9876543210

Output:

Original Number : Masked Number

9876543210 : xxxxxxxxxx

## How to Run

1. Clone this repository.
2. Open the project folder.
3. Update the file path in `number_masking.py` according to the location of your input file.
4. Run the Python program:

```bash
python number_masking.py
