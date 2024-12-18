# импорт библиотек и файлов
import unittest
import runner as rr

# класс Runner, наследуемый от TestCase из модуля unittest
class RunnerTest(unittest.TestCase):

    # метод test_walk
    def test_walk(self):
        # объект класса Runner с произвольным именем
        walk_ = rr.Runner('man')
        # вызов метода walk у этого объекта 10 раз
        for _ in range(10):
            walk_.walk()
        # методом assertEqual сравниваем distance этого объекта со значением 50
        self.assertEqual(walk_.distance, 50)
        # вывод на консоль если все правильно
        print ('Test "walk" OK')

    # метод test_run
    def test_run(self):
        # объект класса Runner с произвольным именем
        run_ = rr.Runner('man')
        # вызов метода run у этого объекта 10 раз
        for _ in range(10):
            run_.run()
        # методом assertEqual сравниваем distance этого объекта со значением 100
        self.assertEqual(run_.distance, 100)
        # вывод на консоль если все правильно
        print('Test "run" OK')

    # метод test_challenge
    def test_challenge(self):
        # создаются 2 объекта класса Runner с произвольными именами
        challenge1 = rr.Runner('man_R')
        challenge2 = rr.Runner('man_W')
        # 10 раз у объектов вызываются методы run и walk соответственно
        for _ in range(10):
            challenge1.run()
            challenge2.walk()
        # метод assertNotEqual, чтобы убедится в неравенстве результатов
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        # вывод на консоль если все правильно
        print('Test "challenge" OK')

if __name__ == '__main__':
    unittest.main()       
