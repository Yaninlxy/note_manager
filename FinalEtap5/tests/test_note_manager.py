import unittest
from FinalEtap5.data import save_notes_to_file, load_notes_from_file
from FinalEtap5.utils import validate_date, validate_status, generate_unique_id

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [{"title": "Test", "content": "Test content"}]
        save_notes_to_file(notes, 'test_notes.txt')
        loaded_notes = load_notes_from_file('test_notes.txt')
        self.assertEqual(notes, loaded_notes)

    def test_validate_date(self):
        self.assertTrue(validate_date("15-01-2025"))
        self.assertFalse(validate_date("2025-01-15"))

    def test_validate_status(self):
        self.assertTrue(validate_status("новая"))
        self.assertFalse(validate_status("старый статус"))

    def test_generate_unique_id(self):
        id1 = generate_unique_id()
        id2 = generate_unique_id()
        self.assertNotEqual(id1, id2)

if __name__ == "__main__":
    unittest.main()
