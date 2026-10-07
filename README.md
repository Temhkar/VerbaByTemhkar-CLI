# VerbaByTemhkar CLI

#### Video Demo: https://youtu.be/dCVc9IhLq5E?si=SqulyLHLcB4PXmMq

## Overview / About the Project

The main idea of my program was learning new (for instance, English) words faster, creating and editing your own dictionary of new words, and keeping track of your statistics progress. I've implemented a program that has a game menu, and the user can choose by themselves what they want to do.

## File Structure & Functionality

### project.py
That's the main file in my project — the program's brain, in other words.

Here's a `main()` function that opens a game menu to the user with some scenarios:
1. In the 1st scenario, the user starts a game quiz.
2. In the 2nd scenario, the user can add new words and translations to the dictionary.
3. In the 3rd scenario, the user can check their statistics.
4. In the 4th scenario, the user can remove all data, like clearing the dictionary and resetting statistics.
5. In the 5th scenario, the user can just quit the program.

Besides the `main()` function, there are equally important functions like:
* `clean_input()` — Edits all text that the user writes in the program's console. This function transforms strings to lowercase to avoid case mismatches, and handles cases where the user accidentally types spaces before or after a word.
* `check_answer()` — Checks the user's answer by taking into consideration the `clean_input()` function, ignoring case or spaces before/after the answer.
* `calculate_score()` — Counts the user's score after a quiz and prints the percentage of correct answers by dividing the number of correct answers by the total number of words asked, rounding the result, and converting it to a percentage.

#### Scenarios Details:
1. **`run_quiz()`** — Starts a game where the program gives the user a word in Russian and expects the correct word in English. If the word is correct, the program adds +1 to the score and prints the next word. If not, the program gives the user one more attempt. After 2 mistakes, the program reveals the correct answer and shows the next word. At the end of the quiz, the program shows the user's score with percentages.
2. **`add_word()`** — Allows the user to add words to the dictionary. The program requests an English word from the user and validates via the Free Dictionary API whether the word exists. If the word exists, the program requests the Russian translation. After that, the new word is added to the dictionary and saved in the `words.csv` file. If the word doesn't exist (i.e., not in the API dictionary), the program raises an error stating that the word doesn't exist.
3. **`show_statistics()`** — Prints a beautifully formatted table in the console showing the history of all the user's games. All statistics data is stored in the `statistics.csv` file across 3 columns: date of game, score (correct answers/total questions), and Russian words where the user made a mistake. Statistics formatting is handled per the installed `tabulate` library.
4. **`clear_data()`** — If the user wants to start fresh, they can clear all data by removing all words in their dictionary (clears `words.csv`) and resetting their statistics (clears `statistics.csv`). Before deleting progress, the program asks twice for confirmation. Typing "y" means yes, and typing "n" means no.
5. **Exit** — Breaks the `while True` loop in the `main()` function and exits the program.

### test_project.py
This file contains automated tests that check the correct work of functions `clean_input()`, `check_answer()`, and `calculate_score()` in the `project.py` file.

### requirements.txt
Here is the list of third-party libraries:
* `requests` — for network requests.
* `tabulate` — for formatting tables.

### words.csv & statistics.csv
* `words.csv` — User's dictionary. Includes a list of words and their translations.
* `statistics.csv` — Includes all quiz history across three columns (date, score, mistaken words).

## Design Choices

* **Word Validation via API (`requests`):** I decided to use the Free Dictionary API for adding new words because it helps avoid the problem of adding incorrect or non-existent words.
* **Formatted Table Output (`tabulate`):** To show user statistics more beautifully, I decided to use the `tabulate` library. It helps print a readable table in the program's console, unlike ugly text split by commas.
* **Data Storage via CSV:** For files where information like words and statistics are saved, I chose CSV files because they have a simple format, don't require complex databases, and are easy to read and save between launches.

## How to Run the Project

1. Create and activate a virtual environment (optional):
   * macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Windows:
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run unit tests via pytest:
    pytest test_project.py

4. Launch the application:
    python project.py
