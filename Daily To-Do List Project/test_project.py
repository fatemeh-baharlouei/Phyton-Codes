import pytest
import csv
import os
import project
from unittest.mock import patch, mock_open
from datetime import date


CSV_FILE = "test_to_do.csv"
FIELDNAMES = ["No.", "Task", "Duration", "Done?"]


def test_get_today_date():
        today_date = date.today().strftime("%B %d, %Y")
        assert project.get_today_date() == today_date

@pytest.fixture
def create_csv():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
    yield
    os.remove(CSV_FILE)


def test_initialize_csv_file():
    with patch("builtins.open", mock_open()) as mockfile:
        project.initialize_csv_file(CSV_FILE)
        mockfile.assert_called_once_with(CSV_FILE, "w", newline="")
        handle = mockfile()
        handle.write.assert_called_once_with(",".join(FIELDNAMES) + "\r\n")


def test_add_task(monkeypatch, create_csv):
    monkeypatch.setattr("builtins.input", lambda _: "Python project")
    project.add_task(CSV_FILE)
    with open(CSV_FILE, "r") as file:
        rows = list(csv.DictReader(file))
        assert len(rows) == 1
        assert rows[0]["Task"] == "Python project"


def test_delete_task(monkeypatch, create_csv):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({"No.": 1, "Task": "1", "Duration": "_", "Done?": "_"})
    monkeypatch.setattr("builtins.input", lambda _: "1")
    project.delete_task(CSV_FILE)
    with open(CSV_FILE, "r") as file:
        rows = list(csv.DictReader(file))
        assert len(rows) == 0


def test_task_done(monkeypatch, create_csv):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({"No.": 1, "Task": "Task 1", "Duration": "_", "Done?": "_"})
    inputs = iter(["1", "15"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    project.task_done(CSV_FILE)
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert rows[0]["Duration"] == "15"
        assert rows[0]["Done?"] == "Done."


def test_print_list(capsys, create_csv):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({"No.": 1, "Task": "1", "Duration": "_", "Done?": "_"})
    project.print_list(CSV_FILE)
    captured = capsys.readouterr()
    assert "1" in captured.out
    

def cleanup():
    yield
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)