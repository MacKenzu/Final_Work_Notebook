from Service.Read import read_notes


def list_notes():
    notes = read_notes()
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Содержимое: {note['body']}")
            print(f"Дата/время создания или последнего изменения: {note['timestamp']}")
            print()
