import unittest
import emulator

class TestEmulator(unittest.TestCase):
    def setUp(self):
        # Инициализируем тестовую файловую систему перед каждым тестом
        emulator.vfs_paths = ["Documents/", "Documents/file.txt", "Downloads/", "Pictures/"]
        emulator.current_dir = ""

    def test_cd_success(self):
        """Проверка успешного перехода в существующую папку"""
        error_msg = emulator.cmd_cd(["Documents"])
        self.assertEqual(error_msg, "")
        self.assertEqual(emulator.current_dir, "Documents/")

    def test_cd_fail(self):
        """Проверка перехода в несуществующую папку"""
        error_msg = emulator.cmd_cd(["FakeFolder"])
        self.assertEqual(error_msg, "cd: FakeFolder: Нет такого каталога")
        self.assertEqual(emulator.current_dir, "")

    def test_cd_back(self):
        """Проверка возврата на уровень назад (cd ..)"""
        emulator.current_dir = "Documents/"
        emulator.cmd_cd([".."])
        self.assertEqual(emulator.current_dir, "")

    def test_cd_root(self):
        """Проверка возврата в корень (cd ~)"""
        emulator.current_dir = "Documents/"
        emulator.cmd_cd(["~"])
        self.assertEqual(emulator.current_dir, "")

    def test_execute_exit(self):
        """Проверка команды exit"""
        should_continue, has_error = emulator.execute_command("exit", "test_log.csv")
        self.assertFalse(should_continue)
        self.assertFalse(has_error)

    def test_execute_syntax_error(self):
        """Проверка незакрытых кавычек"""
        should_continue, has_error = emulator.execute_command("cd \"Documents", "test_log.csv")
        self.assertTrue(should_continue)
        self.assertTrue(has_error)

if __name__ == '__main__':
    unittest.main()