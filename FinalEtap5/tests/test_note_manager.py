import unittest
from data import save_notes_to_file, load_notes_from_file
from utils import validate_date, validate_status, generate_unique_id


class TestNoteManager(unittest.TestCase):

    def setUp(self):
        """
        Подготовка тестовых данных.
        """
        self.notes = [
            {
                "username": "Тестовый пользователь",
                "title": "Тестовая заметка",
                "content": "Описание заметки",
                "status": "новая",
                "created_date": "01-01-2025",
                "issue_date": "10-01-2025",
            }
        ]
        self.test_file = "test_notes.txt"

    def tearDown(self):
        """
        Удаление тестового файла после тестов.
        """
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_notes(self):
        """
        Тестирование сохранения и загрузки заметок.
        """
        save_notes_to_file(self.notes, self.test_file)
        loaded_notes = load_notes_from_file(self.test_file)
        self.assertEqual(self.notes, loaded_notes)

    def test_validate_date(self):
        """
        Тестирование валидации даты.
        """
        self.assertTrue(validate_date("01-01-2025"))
        self.assertFalse(validate_date("31-02-2025"))

    def test_validate_status(self):
        """
        Тестирование валидации статуса.
        """
        self.assertTrue(validate_status("новая"))
        self.assertFalse(validate_status("недопустимый статус"))

    def test_generate_unique_id(self):
        """
        Тестирование генерации уникального идентификатора.
        """
        unique_id = generate_unique_id()
        self.assertIsInstance(unique_id, str)
        self.assertTrue(len(unique_id) > 0)


if __name__ == "__main__":
    unittest.main()
