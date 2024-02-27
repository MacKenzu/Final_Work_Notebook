
from Service.List import list_notes
from Service.Add import add_note
from Service.Edit import edit_note
from Service.Delete import delete_note





def main():
    while True:
        print("Выберите действие:")
        print("1. Просмотреть список заметок")
        print("2. Добавить новую заметку")
        print("3. Отредактировать существующую заметку")
        print("4. Удалить заметку")
        print("0. Выйти")

        choice = input("Введите номер действия: ")
        print()

        if choice == '1':
            list_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '0':
            break
        else:
            print("Некорректный ввод. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()