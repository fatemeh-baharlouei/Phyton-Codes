import csv
import sys
from datetime import date
from tabulate import tabulate


CSV_FILE = "to_do.csv"
FIELDNAMES = ["No.", "Task", "Duration", "Done?"]


def main():
    csv_file = "to_do.csv"
    initialize_csv_file(csv_file)
    today_date = get_today_date()
    print(f"\nHi, today is {today_date}, and here is your today's TO-DO list.\nPlease enter your tasks and mark them when you've done them.")
    while True:
        get_action(csv_file)
        print_list(csv_file)


def initialize_csv_file(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()


def get_today_date():
    today_date = date.today()
    today_date = today_date.strftime("%B %d, %Y")
    return today_date


def get_action(csv_file):
    action = input("\n1.Add task.\n2.Delete task.\n3.Task done.\n4.Exit.\n\n")
    if action == "1":
        add_task(csv_file)
    elif action == "2":
        delete_task(csv_file)
    elif action == "3":
        task_done(csv_file)
    elif action == "4":
        exit_program()


def add_task(csv_file):
    with open(csv_file, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        i = last_task_number(csv_file) +1

        while True:
            task = input(f"\nTask{i}: ")
            writer.writerow({"No.": i, "Task": task, "Duration": "_", "Done?": "_"})
            cont = input("Do you want to add more tasks (yes/no)? ").lower().strip()
            if cont != "yes":
                break
            i +=1


def last_task_number(csv_file):
    try:
        with open(csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if rows:
                return int(rows[-1]["No."])
            return 0
    except:
        return 0


def delete_task(csv_file):
    try:
        row_number = int(input("\nEnter the task number that want to delete: "))
        rows = get_rows(csv_file)
        if 1 <= row_number <= len(rows):
            del rows[row_number - 1]
            rewrite_csv(rows, csv_file)
            print("\nTask deleted successfully.\n")
        else:
            print("\nInvalid task number. Please try again.\n")
    except ValueError:
        print("\nInvalid input. Please enter a valid task number.\n")   
    

def task_done(csv_file):
    try:
        row_number = int(input("\nEnter the task number that you've done: "))
        rows = get_rows(csv_file)
        if 1 <= row_number <= len(rows):
            duration = int(input("Duration (min): "))
            rows[row_number - 1]["Duration"] = duration    
            rows[row_number - 1]["Done?"] = "Done."
            rewrite_csv(rows, csv_file)
            print("\nTask marked as done successfully.\n")
        else:
            print("\nInvalid task number. Please try again.\n")
    except ValueError:
        print("\nInvalid input. Please enter a valid task number.\n")


def get_rows(csv_file):
    try:
        with open(csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def rewrite_csv(rows, csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        i = 1
        for row in rows:
            row["No."] = i
            writer.writerow(row)
            i += 1
    

def print_list(csv_file):
    rows = get_rows(csv_file)
    if rows:
        print(tabulate(rows, headers="keys", tablefmt="grid", numalign="center", stralign="center"))
    else:
        print("\nNo tasks found.")


def exit_program():
    sure = input("\nAre you sure you want to exit? ").lower().strip()
    if sure == "yes":
        sys.exit()


if __name__ == "__main__":
    main()