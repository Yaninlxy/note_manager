import unittest


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        """
        Подготовка перед каждым тестом: создаем тестовые данные.
        """
        self.notes = [
            {
                "username": "Alex",
                "title": "Shop List",
                "content": "Buy milk",
                "status": "new",
                "created_date": "18-01-2025",
                "issue_date": "18-01-2025"
            },
            {
                "username": "Anna",
                "title": "Meeting Notes",
                "content": "Discuss project milestones.",
                "status": "in progress",
                "created_date": "19-01-2025",
                "issue_date": "20-01-2025"
            }
        ]
        self.test_file = "test_notes.txt"

    def test_validate_note_valid(self):
        """
        Проверка корректных данных для валидации.
        """
        valid_note = self.notes[0]
        self.assertTrue(valid_note(valid_note))

    def test_validate_note_invalid(self):
        """
        Проверка некорректных данных для валидации.
        """
        invalid_note = {
            "username": "",
            "title": "Title without user",
            "content": "No username provided.",
            "status": "unknown",
            "created_date": "invalid_date",
            "issue_date": ""
        }
        self.assertFalse(validate_note(invalid_note))

    def test_save_and_load_notes(self):
        """
        Проверка сохранения и загрузки заметок.
        """
        save_notes_to_file(self.notes, self.test_file)
        loaded_notes = load_notes_from_file(self.test_file)
        self.assertEqual(self.notes, loaded_notes)

    def test_display_notes(self):
        """
        Проверка корректного отображения заметок.
        """
        from io import StringIO
        import sys

        # Перехватываем стандартный вывод
        captured_output = StringIO()
        sys.stdout = captured_output

        display_notes(self.notes)

        # Проверяем, что текст заметок содержится в выводе
        output = captured_output.getvalue()
        self.assertIn("Shopping List", output)
        self.assertIn("Discuss project milestones.", output)

        # Восстанавливаем стандартный вывод
        sys.stdout = sys.__stdout__

    def tearDown(self):
        """
        Очистка после каждого теста: удаляем тестовые файлы.
        """
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
