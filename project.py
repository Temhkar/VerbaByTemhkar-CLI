import csv
import requests
from datetime import date
from tabulate import tabulate


def main():
    try:
        while True:
            print("Select a game mode:\n1 - Start the game\n2 - Add words\n3 - Show statistics\n4 - Clear all data\n5 - Exit the game")
            select_mode = int(input("Game mode: "))
            if not (1 <= select_mode <= 5):
                pass
            else:
                if select_mode == 1:
                    run_quiz()
                elif select_mode == 2:
                    add_word()
                elif select_mode == 3:
                    show_statistics()
                elif select_mode == 4:
                    clear_data()
                else:
                    print("Goodbye :)")
                    break
    except ValueError:
        print("Invalid input")

def clean_input(text):
    if not isinstance(text, str):
        return ""
    else:
        text = text.strip().lower()
        return text

def check_answer(user_input, correct_answer):
    user_input = clean_input(user_input)
    correct_answer = clean_input(correct_answer)
    if user_input == correct_answer:
        return True
    else:
        return False

def calculate_score(correct, total):
    if total <= 0:
        return "0 / 0 (0%)"
    else:
        percentage = round((correct / total) * 100)
        return f"{correct} / {total} ({percentage}%)"



def run_quiz():
    wrong_words = []
    try:
        with open("words.csv", mode="r") as file:
            reader = csv.reader(file)
            words_list = list(reader)
        if len(words_list) == 0:
            print("No words in the dictionary\n")
            return ""
        else:
            score = 0
            for row in words_list:
                word = row[0]
                translation = row[1]
                print(f"Translate to English: {translation}")
                for attempt in range(2):
                    user_answer = clean_input(input("Answer: "))
                    if check_answer(user_answer, word):
                        score += 1
                        print("Correct!")
                        break
                    else:
                        if attempt == 0:
                            print("Try again")
                        else:
                            print(f"Incorrect. {translation} = {word}")
                            wrong_words.append(translation)

            total_words = len(words_list)
            percentage = calculate_score(score, total_words)

            if len(wrong_words) > 0:
                wrong_str = ", ".join(wrong_words)
            else:
                wrong_str = "-"

            today = date.today().strftime("%Y-%m-%d")
            with open("statistics.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([today, percentage, wrong_str])

            print(percentage)




    except FileNotFoundError:
        print("No words in the dictionary\n")
        return ""


def add_word():
    word = input("Enter an English word: ")
    word = clean_input(word)

    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if not (response.status_code == 200):
        print("Non-existent word\n")
        return ""
    else:
        translation = input("Enter the translation of this word: ")
        translation = clean_input(translation)
        with open("words.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([word, translation])
        print("New words were added!\n")


def show_statistics():
    statistics_data = []
    try:
        with open("statistics.csv", mode="r") as file:
            reader = csv.reader(file)
            statistics_list = list(reader)
        if len(statistics_list) == 0:
            print("There are no statistics yet\n")
            return ""
        else:
            for row in statistics_list:
                statistics_data.append({"Date": row[0], "Score": row[1], "Mistakes": row[2]})

        print(tabulate(statistics_data, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        print("There are no statistics yet\n")
        return ""


def clear_data():
    sure = input("Are you sure you want to clear all data? (y/n): ")
    if sure == "y":
        with open("words.csv", mode="w") as file:
            pass
        with open("statistics.csv", mode="w") as file:
            pass
        print("Data cleared successfully\n")
    elif sure == "n":
        print("Cancelled\n")
        return
    else:
        print("Invalid input\n")
        return



if __name__ == "__main__":
    main()
