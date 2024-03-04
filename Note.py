import csv
import datetime

def save_note(note):
    with open('notes.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(note)

def read_notes():
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(f'ID: {row[0]}')
            print(f'Title: {row[1]}')
            print(f'Content: {row[2]}')
            print(f'Date: {row[3]}')
            print()

def add_note():
    # id = str(input("Введите идентификатор заметки: "))
    title = input('Введите заголовок заметки: ')
    content = input('Введите тело заметки: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = [generate_id(), title, content, date]
    save_note(note)
    print('Заметка успешно сохранена')


def edit_note():
    note_id = input('Введите ID заметки для редактирования: ')
    new_title = input('Введите новый заголовок заметки: ')
    new_content = input('Введите новое тело заметки: ')
    updated_notes = []
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] == note_id:
                updated_notes.append([row[0], new_title, new_content, str(datetime.datetime.now())])
            else:
                updated_notes.append(row)
    with open('notes.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(updated_notes)
    print('Заметка успешно отредактирована')


def delete_note():
    note_id = input('Введите ID заметки для удаления: ')
    remaining_notes = []
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != note_id:
                remaining_notes.append(row)
    with open('notes.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(remaining_notes)
    print('Заметка успешно удалена')


def generate_id():
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        last_id = 0
        for row in reader:
            last_id = int(row[0])
        return str(last_id + 1)


def main():
    while True:
        command = input('Введите команду (add, edit, delete, read, readAll, exit ): ')
        if command == 'add':
            add_note()
        elif command == 'edit':
            edit_note()
        elif command == 'delete':
            delete_note()
        elif command == 'read':
            read_notes()
        elif command == 'readall':
            read_notes()
        elif command == 'exit':
            break
        else:
            print('Некорректная команда')


if __name__ == '__main__':
    main()
