"""
display_notes_function.py
Функция для отображения всех заметок.
"""

def display_notes(notes):
    """Отображение всех заметок."""
    if not notes:
        print("Нет доступных заметок.")
        return

    for idx, note in enumerate(notes, 1):
        print(f"\nЗаметка #{idx}")
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
    ]
    display_notes(notes)
