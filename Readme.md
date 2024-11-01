# Norwegian Flash Cards

A console-based program for practicing Norwegian vocabulary by translating between English and Norwegian. Users can test their knowledge with the top 1000 most common words in Norwegian, either in a sequential order or through random selection.

## Features

- Translation Practice:
  - Guess English words from Norwegian.
  - Guess Norwegian words from English.
  - Choose to practice in a sequential order (words 1–1000) or with random words.

## How to Use

1. Run the Program: Start the program by executing `python flashcards.py` in a Python environment.

2. Select Practice Mode: After launching, the following practice options are available:

   - [1] Guess English words from Norwegian in order from 1-1000
   - [2] Guess Norwegian words from English in order from 1-1000
   - [3] Guess English words from Norwegian at random
   - [4] Guess Norwegian words from English at random

3. Answer Prompts: For each word, type your answer and press Enter.
   - If correct, the program will display “correct.”
   - If incorrect, the program will show the correct answer and prompt you to press a key to continue.

## Prerequisites

- Python 3 is required to run the program.
- CSV File Provided: The `norsk.csv` file is included with the program and contains the top 1000 Norwegian words.

## CSV Structure

The `norsk.csv` file is formatted with the following columns:

ID, Norwegian, English

Example:

1, hund, dog
2, kat, cat
...

## Dependencies

- CSV module: For handling CSV file data.
- OS module: To clear the screen and pause after incorrect answers.
- Random module: For selecting random words during practice.

## Code Overview

- `main()`: Displays menu options and prompts for user selection.
- `english_from_norwegian(row)`: Prompts for English translation of a Norwegian word.
- `norwegian_from_english(row)`: Prompts for Norwegian translation of an English word.
- `display_rows_sequence(choice)`: Loops through words in sequential order based on choice.
- `display_rows_random(choice)`: Selects random words based on choice.
- `read_rows()`: Loads word data from `norsk.csv`.

## Contributing

Feel free to contribute by adding features, refactoring, or expanding functionality.

## License

This project is open-source and free to use. Please refer to the LICENSE file for more details.
