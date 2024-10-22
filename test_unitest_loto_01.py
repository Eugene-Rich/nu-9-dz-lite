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

    def test_str01(self):

        tip = True
        nam = 'Comp'
        str1 = str(Playr(tip, nam))
        self.assertEqual(str1, f'Тип игрока : {"Компьютер" if tip else "Человек"} Имя игрока : {nam}')

    def test_eq01(self):

        tip1 = True
        nam1 = 'Comp'
        pl1 = str(Playr(tip1, nam1))
        tip2 = True
        nam2 = 'Comp'
        pl2 = str(Playr(tip2, nam2))
        self.assertEqual(pl1, pl2)

    def test_ne01(self):

        tip1 = True
        nam1 = 'Comp'
        pl1 = str(Playr(tip1, nam1))
        tip2 = False
        nam2 = 'People'
        pl2 = str(Playr(tip2, nam2))
        self.assertNotEqual(pl1, pl2)



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
            self.assertNotEqual(tekb, vbo)
            vbo.append(tekb)

    def test_str01(self):
        m1 = Mbchnk()
        str1 = str(m1)
        self.assertEqual(str1, f'Мешок с бочонками от 1 до 90. Вытянуты бочонки {[i+1 for i in range(0, 90) if m1.masb[i] < 0]}')

    def test_eq01(self):
        m1 = Mbchnk()
        m2 = Mbchnk()
        self.assertEqual(m1, m2)

    def test_ne01(self):
        m1 = Mbchnk()
        m2 = Mbchnk()
        m2.oshbsh()
        self.assertNotEqual(m1, m2)


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

    def test_str01(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        s1 = str(k1)
        self.assertEqual(s1, f'Карточка {k1.name_k} {"закрыта полностью" if k1.krt_is_clouse() else "не закрыта"}')

    def test_eq01(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        s1 = str(k1)
        p2 = Playr(True,'Comp')
        m2 = Mbchnk()
        k2 = Kart(p1, m1)
        s2 = str(k1)
        self.assertEqual(s1, s2)

    def test_ne01(self):
        p1 = Playr(True,'Comp')
        m1 = Mbchnk()
        k1 = Kart(p1, m1)
        s1 = str(k1)
        p2 = Playr(False,'Peopl')
        m2 = Mbchnk()
        k2 = Kart(p2, m2)
        s2 = str(k2)
        self.assertNotEqual(s1, s2)
