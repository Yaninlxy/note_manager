import json

def save_notes_to_file(notes, filename):
    with open(filename, 'w') as file:
        for note in notes:
            file.write(f"{note}\n")

def load_notes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def append_notes_to_file(note, filename):
    with open(filename, 'a') as file:
        file.write(f"{note}\n")

def save_notes_json(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file)
