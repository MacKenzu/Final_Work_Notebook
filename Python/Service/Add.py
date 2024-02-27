import datetime
from Service.Read import read_notes
from Service.Save import save_notes


def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите содержимое заметки: ")
    timestamp = str(datetime.datetime.now())

    notes = read_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена")