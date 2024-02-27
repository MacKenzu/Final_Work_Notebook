import json

def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return []


