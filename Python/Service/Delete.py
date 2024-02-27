from Service.Read import read_notes
from Service.Save import save_notes

def delete_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return

    print("Заметка с указанным ID не найдена")