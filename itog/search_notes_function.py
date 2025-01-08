"""
search_notes_function.py
Функция для поиска заметок.
"""

def search_notes(notes, keyword=None, status=None):
    """Поиск заметок."""
    results = []
    for note in notes:
        if keyword and keyword.lower() not in (note["title"].lower() + note["content"].lower() + note["username"].lower()):
            continue
        if status and status.lower() != note["status"].lower():
            continue
        results.append(note)

    if not results:
        print("Заметки, соответствующие запросу, не найдены.")
    else:
        print("\nНайденные заметки:")
        for idx, note in enumerate(results, 1):
            print(f"\nЗаметка #{idx}")
            for key, value in note.items():
                print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
    ]
    found_notes = search_notes(notes, keyword='покупок')
