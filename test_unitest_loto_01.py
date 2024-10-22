import unittest
from loto import Playr, Mbchnk, Kart

# Тестирование класса "Игрок"

class Test_Playr(unittest.TestCase):

    def test_init01(self):

        tip = False
        nam = 'People'
        p1 = Playr(tip, nam)
        self.assertEqual(p1.typ_p, tip)
        self.assertEqual(p1.name_p, nam)

    def test_init02(self):

        tip = True
        nam = 'Comp'
        p1 = Playr(tip, nam)
        self.assertEqual(p1.typ_p, tip)
        self.assertEqual(p1.name_p, nam)

# Тестирование класса "Мешок"
class Test_Mbchnk(unittest.TestCase):

    # В мешке должны быть бочонки от 1 до 90, отсортированные по возрастанию
    def test_init01(self):
        m1 = Mbchnk()
        self.assertEqual(m1.masb, [i for i in range(1, 91)])

    # Номер очередного бочонка должен быть в пределах от 1 до 90
    def test_oshbsh01(self):
        m1 = Mbchnk()
        for i in range(1, 91):
            tekb = m1.oshbsh()
            self.assertIn(tekb, [i for i in range(1, 91)])

   # Номера бочонков не должны повторяться
    def test_oshbsh02(self):
        m1 = Mbchnk()
        vbo = [] # массив вынутых бочонков
        for i in range(1, 91):
            tekb = m1.oshbsh()
            self.assertNotIn(tekb, vbo)
            vbo.append(tekb)

# Тестирование класса "Карточка"
class Test_Kart(unittest.TestCase):

    # В карточке должно быть 3 строки
    def test_init01(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        self.assertEqual(len(k1.tkart), 3)

    # В каждой строке карточки 9 элементов
    def test_init02(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        self.assertEqual(len(k1.tkart[0]), 9)
        self.assertEqual(len(k1.tkart[1]), 9)
        self.assertEqual(len(k1.tkart[2]), 9)

    # Элементы карточки не должны повторяться
    def test_init03(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        vsk = []
        for i in range(0, 3):
            for j in range(0,9):
                vsk.append(k1.tkart[i][j])

        vsk.sort()
        self.assertEqual(vsk, list(set(vsk)))
