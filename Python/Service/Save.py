import json 

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)