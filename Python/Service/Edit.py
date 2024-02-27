import datetime
from Service.Read import read_notes
from Service.Save import save_notes


def edit_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))

    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое содержимое заметки: ")
            note['timestamp'] = str(datetime.datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return

    print("Заметка с указанным ID не найдена")