class NoteManager:
    def __init__(self):
        self.notes = []
        self.id_counter = 1

    def create_note(self, name, title, description, status, creation_date, deadline):
        if not self.check_unique_title(title):
            print(f"Заголовок '{title}' уже существует. Пожалуйста, выберите другой.")
            return
        
        note = {
            'id': self.id_counter,
            'name': name,
            'title': title,
            'description': description,
            'status': status,
            'creation_date': creation_date,
            'deadline': deadline
        }
        self.notes.append(note)
        self.id_counter += 1
        print(f"Заметка '{title}' успешно создана.")

    def display_notes(self):
        if not self.notes:
            print("Нет созданных заметок.")
            return
        
        print("\nСписок всех заметок:")
        for note in self.notes:
            print(f"ID: {note['id']}, Name: {note['name']}, Title: {note['title']}, "
                  f"Description: {note['description']}, Status: {note['status']}, "
                  f"Creation Date: {note['creation_date']}, Deadline: {note['deadline']}")

    def check_unique_title(self, title):
        for note in self.notes:
            if note['title'] == title:
                return False
        return True

    def delete_note_by_title(self, title):
        for note in self.notes:
            if note['title'] == title:
                self.notes.remove(note)
                print(f"Заметка '{title}' успешно удалена.")
                return
        print(f"Заметка с заголовком '{title}' не найдена.")

    def delete_note_by_name(self, name):
        for note in self.notes:
            if note['name'] == name:
                self.notes.remove(note)
                print(f"Заметка пользователя '{name}' успешно удалена.")
                return
        print(f"Заметка пользователя с именем '{name}' не найдена.")

    def delete_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                print(f"Заметка с ID '{note_id}' успешно удалена.")
                return
        print(f"Заметка с ID '{note_id}' не найдена.")

# Пример использования программы
note_manager = NoteManager()

print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

while True:
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    
    # Ввод даты в формате день-месяц-год
    creation_date = input("Введите дату создания (дд-мм-гггг): ")
    deadline = input("Введите дедлайн (дд-мм-гггг): ")
    
    note_manager.create_note(name, title, description, status, creation_date, deadline)

    add_another = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if add_another != "да":
        break

# Отображение всех заметок после завершения ввода
note_manager.display_notes()
