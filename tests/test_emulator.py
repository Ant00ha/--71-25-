import unittest
import sys
import os
import argparse

# Добавляем папку src в путь, чтобы импортировать emulator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import emulator

class TestStage1(unittest.TestCase):
    def test_repl_and_exit(self):
        """Этап 1: REPL, парсер и команда exit"""
        should_continue, has_error = emulator.execute_command("exit", "test_log.csv")
        self.assertFalse(should_continue)

    def test_parser_quotes(self):
        """Этап 1: Обработка аргументов в кавычках"""
        # Симулируем незакрытую кавычку
        should_continue, has_error = emulator.execute_command('cd "bad path', "test_log.csv")
        self.assertTrue(has_error)

class TestStage2(unittest.TestCase):
    def test_logging_csv(self):
        """Этап 2: Логирование в CSV"""
        log_path = "test_log.csv"
        if os.path.exists(log_path):
            os.remove(log_path)
        emulator.execute_command("fake_command", log_path)
        self.assertTrue(os.path.exists(log_path))

class TestStage3(unittest.TestCase):
    def setUp(self):
        emulator.vfs_paths = ["folder1/", "folder1/file.txt", "folder2/"]
        emulator.current_dir = ""

    def test_vfs_cd(self):
        """Этап 3: Навигация по VFS"""
        emulator.cmd_cd(["folder1"])
        self.assertEqual(emulator.current_dir, "folder1/")
        
    def test_vfs_cd_fail(self):
        """Этап 3: Ошибка при переходе в несуществующую папку"""
        err = emulator.cmd_cd(["bad_folder"])
        self.assertTrue("Нет такого каталога" in err)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Запуск тестов по этапам")
    parser.add_argument('stage', type=int, choices=[1, 2, 3], help="Номер этапа для тестирования (1, 2 или 3)")
    args = parser.parse_args()

    # Формируем набор тестов в зависимости от выбранного этапа
    suite = unittest.TestSuite()
    if args.stage == 1:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStage1))
    elif args.stage == 2:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStage2))
    elif args.stage == 3:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStage3))

    print(f"=== Запуск тестов для Этапа {args.stage} ===")
    unittest.TextTestRunner(verbosity=2).run(suite)