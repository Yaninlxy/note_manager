import unittest
from data import save_notes_to_file, load_notes_from_file
from utils import validate_date, validate_status, generate_unique_id
from interface import display_notes


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.notes = [
            {"id": generate_unique_id(), "title": "Test Note", "content": "This is a test", "status": "новая"}
        ]
        self.file_path = "test_notes.json"

    def test_save_and_load_notes(self):
        save_notes_to_file(self.notes, self.file_path)
        loaded_notes = load_notes_from_file(self.file_path)
        self.assertEqual(self.notes, loaded_notes)

    def test_validate_date(self):
        self.assertTrue(validate_date("01-01-2023"))
        self.assertFalse(validate_date("31-02-2023"))

    def test_validate_status(self):
        self.assertTrue(validate_status("новая"))
        self.assertFalse(validate_status("неизвестная"))

    def test_generate_unique_id(self):
        id1 = generate_unique_id()
        id2 = generate_unique_id()
        self.assertNotEqual(id1, id2)

    def test_display_notes(self):
        try:
            display_notes(self.notes)
        except Exception as e:
            self.fail(f"display_notes raised an exception: {e}")

    def test_validate_note_valid(self):
        first_note = self.notes[0]
        self.assertTrue(validate_status(first_note["status"]))


if __name__ == "__main__":
    unittest.main()
